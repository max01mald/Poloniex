import time 
import sys,getopt
import datetime
from poloniex import poloniex
from QueuePol import QueuePol
import priceExt
import Tradebook
import TradeHistory
import Ticker
import ChartData



def main(argv):
	
	period = 1
	pair = "BTC_XRP"
	
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
					
	conn = poloniex('PVFWK0WJ-KT0KEXJ2-R9OG2QFB-QJ1MJSNZ', 'b1f2a9c6f224951c27380f709f90d53794a9a2057050202a7f0f88c65b2102169db649d52dab81e3d0dc67b4cc48d7a75bb7282b7c095dcde5d1f41419ea2473')
	
	M_30 = QueuePol(30)
	
	print "Running DOGE 1 BTC checker"
	while True:
		
		'''lastPairPrice = conn.api_query("returnTicker")[pair]["last"]
		
		currentValues = str(conn.api_query("returnTicker"))
		
		Ticker.parser(currentValues)
		
		
		M_30.enqueue(float(lastPairPrice))
		
		print M_30.m_avg'''
		
		'''currentTradeHistory = conn.api_query("returnTradeHistory",{'currencyPair': pair, 'start': 1511207242000, 'end': 1514145293000})
		print currentTradeHistory'''
		
		#currentBook = str(conn.api_query("returnOrderBook",{'currencyPair': pair}))
		#Tradebook.parser(currentBook, pair)
		
			
		currentMarket = str(conn.api_query("returnMarketTradeHistory",{'currencyPair': pair}))
		
		print(currentMarket)
		print(pair)
		TradeHistory.parser(currentMarket, pair)
		
		lapse = 300
		end = time.time()
		start = end -10000
		
		#currentChart = str(conn.api_query("returnChartData", {'currencyPair': pair, 'start': start, 'end': end, 'period': lapse}))
		#ChartData.parser(currentChart)
		
		#print "{:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now()) + " Period: %ss %s  %s " % (period,pair,lastPairPrice)
		time.sleep(1)
		
if __name__ == "__main__":
	main(sys.argv[1:])
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
