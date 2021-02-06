import pandas_market_calendars as pm


nyse = pm.get_calendar('NYSE')
sch = nyse.schedule(start_date = '2012-07-01', end_date = '2020-01-01')
print(sch)



