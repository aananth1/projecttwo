   {{
    config(
        materialized = 'incremental',
        database = 'EXCHANGE_RATES',
        unique_key = 'RatesPK',
        schema = 'SILVER',
        incremental_strategy = 'merge'
    )
   }}


   select 
       _airbyte_unique_key_scd as RatesPK,
       Base, 
       Date,
       Rates:AUD as AUD_Daily_Price,
       Rates:USD as USD_Daily_Price,
       Rates:GBP as GBP_Daily_Price,
       Rates:INR as INR_Daily_Price,
       Rates:BTC as BTC_Daily_Price,
       _airbyte_emitted_at as Row_Start_Datetime,
       _airbyte_end_at as Row_End_datetime,
       _airbyte_active_row as Row_Active_Ind
from 
    {{source('EXCHANGE_RATES', 'exchange_rates_scd')}}

{% if is_incremental() %}
    where Date >= (select max (Date) from {{this}})
{% endif %}