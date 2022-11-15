{{
    config(
        materialized = 'table',
        database = 'EXCHANGE_RATES',
        unique_key = 'RatesPK',
        schema = 'GOLD',
    )
   }}


SELECT
  RATESPK,
  DATE, 
  BASE,
  AUD_DAILY_PRICE,
  ROUND(AVG(AUD_DAILY_PRICE) OVER (
    ORDER BY DATE ROWS BETWEEN 7 PRECEDING AND CURRENT ROW
  ),5) as "7_DAY_AUD_AVG_PRICE",
round((AUD_DAILY_PRICE - LAG(AUD_DAILY_PRICE) OVER (PARTITION BY BASE ORDER BY date))* 100.0 / AUD_DAILY_PRICE,2) AS AUD_percent_change
FROM {{ref('ExchangeRate')}} 
where ROW_ACTIVE_IND = 1

