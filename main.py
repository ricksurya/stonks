import stock as st
import graph as gr
import sys

from typing import List

""" 
IMPORTANT VARIABLES
"""

TICKERS = ["ABBV", "OKTA", "ENPH", "CVS"]

"""
METHODS
"""

def main(): 
    action = sys.argv[1]
    type = sys.argv[2]
    if len(sys.argv) == 3:
        tickers = TICKERS
    else:
        tickers = sys.argv[3:]
    
    if action == "--get":
        getInfo(type, tickers)
    elif action == "--graph":
        gr.graphStocks(type, tickers)
    else:
        raise ValueError("The action=" + action + " is not supported")

def getInfo(infoType: str, tickers: List[str]):
    for ticker in tickers:
        try:
            get(infoType, ticker)
        except Exception:
            raise Exception("ERROR: couldn't perform action on the ticker=" + ticker + " ¯\_(ツ)_/¯")


def get(infoType: str, ticker: str):
    stock = st.Stock(ticker)
    if infoType ==  "price":
        print(stock.getName() + ": " + str(stock.getPrice()))
    elif infoType == "pe":
        print(stock.getName() + ": " + str(stock.getPeRatio()))
    elif infoType == "rsi":
        print(stock.getName() + ": " + str(stock.getRsi()))
    else:
        raise ValueError("The information type=" + infoType + " is not supported")
    
if __name__=="__main__": 
    main() 
