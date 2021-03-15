from Ticker import Ticker
import os
import sys

def GetPairs(level):
    pairs = os.listdir(os.path.dirname(os.path.realpath(__file__)) + "/" + level)
    
    for i in range(len(pairs)-1):
        if "." in str(pairs[i]):
            del pairs[i]
    
    return pairs


def GetTicker(pairs):
    market = []
     
    for pair in pairs:
        ticker = Ticker()
        ticker.ReadM(pair)
        #ticker.PrintM()
        market.append(ticker)
        
    del(ticker)
    
    return market

pairs = GetPairs("Ticker")
market_ticker = GetTicker(pairs)

print(len(market_ticker))

for ticker in market_ticker:
    ticker.GetSentiment()
    break
    ticker.PrintM()
