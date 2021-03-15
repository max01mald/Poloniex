from Ticker.Ticker import Ticker
import os
import sys
import re

def GetPairs(level):
    pairs = os.listdir(os.path.dirname(os.path.realpath(__file__)) + "/" + level)

    out_pairs = []
    for i in range(len(pairs)):
        if "." not in str(pairs[i]) and "cache" not in str(pairs[i]):
            out_pairs.append(pairs[i])

    return out_pairs


def GetTicker(pairs):
    market = []

    for pair in pairs:
        ticker = Ticker()
        ticker.ReadM(pair)
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


