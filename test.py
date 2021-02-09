from DBExtract import DBExtract

extract = DBExtract()

df = extract.json_extract("view", ticker="AAPL", FILE_NAME="BalanceSheet_Liabilities")
print(df)