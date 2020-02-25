import time 
import sys,getopt
import datetime
from poloniex import poloniex
from Algorithms.QueuePol import QueuePol
import priceExt
import Tradebook
import TradeHistory
import Ticker
import ChartData
from ratelimit import limits

def InitializeConnection(argv):
    try:
        opts, args = getopt.getopt(argv,"hp:",["period=",])
    except getopt.GetoptError:
        print 'polob.py -p <periods>'
        sys.exit(2)

        for opt, arg in opts:
                if opt == '-h':
                        print 'polob.py -p <period>'
                        sys.exit()
                elif opt in ("-p", "--period"):
                        if (int(arg) in [300,900,1800,7200,14400,86400]):
                                period = arg
                        else:
                                print 'Poloniec requires periods in 300, 900, 1800, 7200, 14400, 86400 s'
                                sys.exit(2)
    
    key = ""
    secret = ""
    conn = poloniex(key,secret)
    return conn
    
ONE_MINUTE = 60

@limits(calls=6, period=ONE_MINUTE)
def main(argv):

        period = 1
	pair = "BTC_ETH"

        print "Running for Currency: " + pair
						
	conn = InitializeConnection(argv)
	M_30 = QueuePol(30)
	
	while True:
                
                #Saves the Ticker Data for BTC market 
                #This will be part of the logging sweet
                '''     
                currentValues = str(conn.api_query("returnTicker"))
                Ticker.parser(currentValues)
                '''

                #By providing a Currency you can receive live Prices and a 30 position moving average
                #This will be part of live analyis sweet
		'''
		lastPairPrice = conn.api_query("returnTicker")[pair]["last"]
                print "{:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now()) + " Period: %ss %s  %s " % (period,pair,lastPairPrice)

                M_30.enqueue(float(lastPairPrice))
                print "Moving average {0:.{1}f}".format(M_30.m_avg,8)
                '''

                #Selects a certain Currency by pair and writes list of buy and sell orders
                #This will be part of live analyis sweet
                ''' 
                currentBook = str(conn.api_query("returnOrderBook",{'currencyPair': pair}))
                Tradebook.parser(currentBook, pair)
                '''
	        
                #Reads Buys and Sells then writes all > 1 BTC to file
                #This will be part of the live analysis sweet
                '''
                currentMarket = str(conn.api_query("returnMarketTradeHistory",{'currencyPair': pair}))
                TradeHistory.parser(currentMarket, pair)
                '''

                #Writes the Chart Data for a set amount of time 
                #This will be part of the live analysis sweet
                '''
                lapse = 300
		end = time.time()
		start = end -10000
		
		currentChart = str(conn.api_query("returnChartData", {'currencyPair': pair, 'start': start, 'end': end, 'period': lapse}))
		ChartData.parser(currentChart,pair,lapse)
		'''

                time.sleep(30)


if __name__ == "__main__":
	main(sys.argv[1:])
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
