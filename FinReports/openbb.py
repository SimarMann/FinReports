from openbb_terminal.sdk import openbb
from datetime import datetime
from dateutil.relativedelta import relativedelta  

## StockScreen Functions
def stock_load(symbol):
    
    end_date = datetime.now().date()
    start_date = end_date - relativedelta(years = 1)
    start_date = start_date.strftime('%Y-%m-%d')
    
    df = openbb.stocks.load(
        symbol = symbol, 
        start_date = start_date, 
        interval = 1440, 
        end_date =  end_date, 
        prepost = False, 
        source = "YahooFinance", 
        iexrange = "ytd", 
        weekly = True, 
        monthly = False, 
        verbose = True
        ) 
    
    return df

"""
def stocks_quote(symbol):
    df = openbb.stocks.quote(symbol)
    df = df.to_dict()
    first_key = list(df.keys())[0]
    df = df[first_key]
    return df
"""

def fa_overview(symbol):
    df = openbb.stocks.fa.overview(symbol)
    df = df.to_dict()
    df = df[0]
    df['Book total']= hum_format(float(df['Book value'])*(num_format(df['Shares outstanding'])))
    return df

## Requires API_KEY_FINANCIALMODELINGPREP
def fa_metrics(symbol):
    df = openbb.stocks.fa.metrics(symbol, 1, False)
    df = df.to_dict()
    first_key = list(df.keys())[0]
    df = df[first_key]
    return df

def fa_income(symbol):
    df = openbb.stocks.fa.income(symbol, False, False, "YahooFinance", 1)
    df = df.iloc[:, 0]
    df = df.to_dict()
    df = (df['Total revenue'] - df['Net income'])
    df = hum_format(df) 
    return df

## Requires API_KEY_FINANCIALMODELINGPREP
def fa_growth(symbol):
    df = openbb.stocks.fa.growth(symbol, 1, False)
    df = df.to_dict()
    first_key = list(df.keys())[0]
    df = df[first_key]   
    return df

## MacroDash Functions
def usbonds():
    bonds = openbb.economy.usbonds()
    bonds = bonds[::-1]
    bonds['Yld (%)'] = bonds['Yld (%)'].astype(float)
    return bonds

def load_futures(symbol):
    end_date = datetime.now().date()
    start_date = end_date - relativedelta(months= 1)
    start_date = start_date.strftime('%Y-%m-%d')
    df = openbb.futures.historical([symbol], "")
    df = df.loc[start_date : end_date]
    df = df.iloc[[0, -1]]
    return (df.iloc[0]['Adj Close'], df.iloc[1]['Adj Close'])

def crypto_1mdelta(symbol):
    end_date = datetime.now().date()
    start_date = end_date - relativedelta(months= 1)
    start_date = start_date.strftime('%Y-%m-%d')
    df = openbb.crypto.load(symbol, start_date, 1440, "binance", "usd", end_date, "YahooFinance")
    df = df.iloc[[0, -1]]
    return df
    

## Formating functions
def hum_format(num):
    num = float('{:.3g}'.format(num))
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), ['', 'K', 'M', 'B', 'T'][magnitude])
    
def num_format(num):
    if type(num) == float or type(num) == int:
        return num
    if 'K' in num:
        if len(num) > 1:
            return float(num.replace('K', '')) * 1000
        return 1000.0
    if 'M' in num:
        if len(num) > 1:
            return float(num.replace('M', '')) * 1000000
        return 1000000.0
    if 'B' in num:
        return float(num.replace('B', '')) * 1000000000
    return 0.0