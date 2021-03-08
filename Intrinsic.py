from DBExtract import DBExtract
from Download import Downloader
from BondRate import BondRate
import pandas as pd
import numpy as np
import statistics as stat

# Criteria
'''DCF Analysis
Any one of these criteria have to be met by stock.
Works rather well on big cap companies such as Apple and Google.
1. Company does not pay any dividends
2. Company pays dividend, but not as much as it can pay
3. Free cash flow aligns with profitability
4. Free cash flow must be positive
'''

DB_PATH = r'C:\Users\Gavin\Desktop\FinData'

def intrinsic(ticker, DB_PATH, estimated_yrs = 4, expected_rate_return = 0.1, perpetual_growth = 0.025, margin_safety = 0.5, download = True):
    # Calculate Intrinsic using DCF Model
    ticker = ticker
    DB_PATH = DB_PATH

    if (download == True):
        # # Download data 
        d = Downloader()
        d.download(type_="string", DB_PATH = DB_PATH, buffer=1, ticker = ticker)

    else:
        pass

    # Pull from database
    e = DBExtract(DB_PATH)
    keydata_df = e.json_extract("view", ticker=ticker, FILE_NAME="KeyData")
    keydata_df_data = e.json_extract("data", ticker=ticker, FILE_NAME="KeyData")
    income_df = e.json_extract("data", ticker=ticker, FILE_NAME="IncomeStatement")
    bal_assets_df = e.json_extract("data", ticker=ticker, FILE_NAME="BalanceSheet_Assets")
    bal_lia_df = e.json_extract("data", ticker=ticker, FILE_NAME="BalanceSheet_Liabilities")
    opr_df = e.json_extract("data", ticker=ticker, FILE_NAME="CashFlow_Operating")
    inv_df = e.json_extract("data", ticker=ticker, FILE_NAME="CashFlow_Investing")
    fin_df = e.json_extract("data", ticker=ticker, FILE_NAME="CashFlow_Financing")

    def div_thousand(number):
        return number/1000

    # Extract Total Cash flow from Operating Activies
    free_cashflow = list(map(div_thousand,e.select_item(opr_df, "Net Operating Cash Flow").tolist()))

    # Extract Capital Expenditures
    capital_exp = list(map(div_thousand,e.select_item(inv_df, "Capital Expenditures").tolist()))

    # Calculate Free Cash Flow to Equity, Total Cash Flow - Capital Expenditures
    fcf_to_eq = []
    for i in range(0, len(free_cashflow)):
        fcf = free_cashflow[i] + capital_exp[i] # Free cash flow to equity
        fcf_to_eq.append(fcf)

    # Extract Net Income
    net_income = list(map(div_thousand,e.select_item(income_df, "Net Income").tolist()))

    # Get FCFE / Net income Ratio
    fcf_ratio = []
    for i in range(0, len(free_cashflow)):
        val = round(fcf_to_eq[i] / net_income[i],5)
        fcf_ratio.append(val)

    # Get Revenue & Rev Growth Rate
    rev = list(map(div_thousand,e.select_item(income_df, "Sales/Revenue").tolist()))
    rev_growth = []
    for i in range(0,len(rev)-1):
        diff = rev[i+1] - rev[i]
        prc_change = round(diff/rev[i],2)
        rev_growth.append(prc_change)
    rev_gr = stat.median(rev_growth)

    # Get profit margins & Net income Growth Rate
    net_income_margins = []
    for i in range(0, len(rev)):
        ratio = round(net_income[i] / rev[i],2)
        net_income_margins.append(ratio)
    net_income_gr = min(net_income_margins)

    # Expected Total Revenue 4 years Estimated
    for i in range(0,estimated_yrs):
        new_rev = round(rev[-1] * (1+rev_gr))
        rev.append(new_rev)

    # Expected Net Income 4 years Estimated
    for i in range(0,estimated_yrs):
        new_net_income = round(net_income[-1] * (1+net_income_gr),2)
        net_income.append(new_net_income)

    # Expected Free Cash Flow 4 years Estimated
    for i in range(0,estimated_yrs):
        # Get index
        index = i-estimated_yrs
        est_fcf = net_income[index] * min(fcf_ratio)
        fcf_to_eq.append(est_fcf)

    # Add estimated 4 years to years column
    columns = [str(col) for col in income_df.columns]
    for i in range(0,estimated_yrs):
        year = int(columns[-1].replace(" Est.", "")) + 1
        est_year = str(year) + " Est."
        columns.append(est_year)

    # --------------
    # Get WACC (Weighted Average Cost of Capital)
    # Formula = Weighted Debt * Cost of Debt + Weighted Equity * Capital Asset Pricing Model
    # --------------
    # Get Cost of Debt
    # Formula = IE / Debt * (1 - taxRate)
    # Tax rate 
    pretax_inc = div_thousand(e.select_item(income_df, "Pretax Income").tolist()[-1])
    inc_tax = div_thousand(e.select_item(income_df, "Income Tax").tolist()[-1])
    tax_rate = round(inc_tax / pretax_inc,4)
    # Interest Expense
    interest_expense = div_thousand(e.select_item(income_df, "Interest Expense").tolist()[-1])
    # Debt
    long_term_debt = div_thousand(e.select_item(bal_lia_df, "Long-Term Debt").tolist()[-1])
    short_term_debt = div_thousand(e.select_item(bal_lia_df, "Current Portion of Long Term Debt").tolist()[-1])
    total_debt = long_term_debt + short_term_debt

    cost_of_debt = round(interest_expense / total_debt * (1 - tax_rate),5)

    # --------------
    # Get Capital Asset Pricing Model
    # Formula = RiskFreeRate + Beta(Avg Expected Rate of Return - RiskFreeRate)
    riskfreerate = BondRate().bondrate()
    expected_return = expected_rate_return
    beta = float(e.select_item(keydata_df, "Beta"))

    capital_asset_pricing_model = round((riskfreerate + beta*(expected_return*100 - riskfreerate))/100,5)
    # --------------

    # Weighted Equity and Weighted Debt
    # Formula = total debt /Debt + marketcap or marketcap / debt + marketcap
    market_cap = div_thousand(e.select_item(keydata_df_data, "Market Cap"))
    weighted_debt = round(total_debt / (market_cap + total_debt),3)
    weighted_equity = round(market_cap / (market_cap + total_debt),3)
    # --------------

    # Get WACC
    print(f'weighted_debt : {weighted_debt}' )
    print(f'cost_of_debt : {cost_of_debt}' )
    print(f'weighted_equity : {weighted_equity}' )
    print(f'capital_asset_pricing_model : {capital_asset_pricing_model}' )

    wacc = round(weighted_debt * (cost_of_debt) + weighted_equity * capital_asset_pricing_model,4)

    # --------------

    # Get shares outstanding
    shares_outstanding = div_thousand(e.select_item(keydata_df_data, "Shares Outstanding"))

    # Perpetual Growth
    p_growth = perpetual_growth

    # Calculate Terminal Value
    terminal_value = round(fcf_to_eq[-1] * (1 + p_growth) / wacc - p_growth)

    # Get discount factor for each year
    discount_factor = []
    for i in range(0, len(free_cashflow)):
        discount_factor.append("NaN")
    for i in range(0, estimated_yrs):
        val = round((1+wacc)**(i+1),3)
        discount_factor.append(val)

    # Get present value of Future Cash Flow
    pv_fcf = []
    for i in range(0, len(free_cashflow)):
        pv_fcf.append(0)
    for i in range(0, estimated_yrs):
        val = round(fcf_to_eq[i-estimated_yrs] * discount_factor[i-estimated_yrs])
        pv_fcf.append(val)

    # Get today's value 
    todays_value = sum(pv_fcf) + terminal_value

    # Intrinsic Value
    intrinsic_value = round(todays_value / shares_outstanding,2)
    # Create DataFrame, Total Rev, Net Income, FCF 
    labels = ["Total Revenue", "Net Income", "Free Cash Flow"]
    df = pd.DataFrame(index = columns, columns = labels)
    df['Total Revenue'] = rev
    df['Net Income'] = net_income
    df['Free Cash Flow'] = fcf_to_eq
    df['Discount Factor'] = discount_factor
    df['PV of Future Cash Flow'] = pv_fcf
    df = df.transpose()

    margin_of_safety = margin_safety
    print(df)
    print(f"Today's Value : ${todays_value}")
    print(f"Intrinsic Value : ${intrinsic_value}")
    print(f"BuyPrice w/ margin of safety : ${round(intrinsic_value * margin_of_safety,2)}")

    return round(intrinsic_value * margin_of_safety,2)

intrinsic("AAPL", DB_PATH, download = True)