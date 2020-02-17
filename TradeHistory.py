import os
import sys

class TradeBook:
	Currency = ""
	type = ""
	tradeID = 0
	amount = 0.0
	rate = 0.0
	am_BTC = 0.0
	date = ""
	globalTradeID = 0
	Trades = []
	
		
	def __init__(self):
		self.Currency = ""
		self.type = ""
		self.tradeID = 0
		self.amount = 0.0
		self.rate = 0.0
		self.am_BTC = 0.0
		self.date = ""
		self.globalTradeID = 0
		self.Trades = []
	
	def Copy(self):
		BookC = TradeBook()
		
		BookC.Currency = self.Currency
		BookC.tradeID = self.tradeID
		BookC.type = self.type
		BookC.amount = self.amount
		BookC.rate = self.rate
		BookC.am_BTC = self.am_BTC
		BookC.date = self.date
		BookC.globalTradeID = self.globalTradeID
		
		return BookC

	def __del__(self):
		self.type = ""
		self.tradeID = 0
		self.amount = 0.0
		self.rate = 0.0
		self.am_BTC = 0.0
		self.date = ""
		self.globalTradeID = 0
		del self.Trades[:]
		
	def PrintBook(self):
		print "%s %s %.8f %.8f %.8f" % (self.Currency, self.type, self.rate, self.amount, self.am_BTC)
	
	def PrintMBook(self):
		
		i=0
		
		while i<len(self.Trades):
			self.Trades[i].PrintBook()
			i+=1

	def Market(self, Book):
			NBook = Book.Copy()
			self.Trades = self.Trades + [NBook]
			
	def WriteBuy(self):
	
		os.chdir("/Users/Max/Desktop/CRYPTO/Poloniex/TradeHistory")
		
		
		if not os.path.exists("/Users/Max/Desktop/CRYPTO/Poloniex/TradeHistory/" + self.Currency):
   			os.makedirs("/Users/Max/Desktop/CRYPTO/Poloniex/TradeHistory/" + self.Currency)
   			
   		os.chdir("/Users/Max/Desktop/CRYPTO/Poloniex/TradeHistory/" + self.Currency)
   			
		name = self.Currency + "_Buys.txt"
			
		
		
		if self.am_BTC > 1:
			fo = open(name, "a+")
			fo.seek(0,0)
			file_data = fo.read()
			fo.seek(0,0)
			fo.truncate()
			s = "%s %s %d %.8f %.8f %.8f" % (self.date, self.Currency, self.globalTradeID, self.amount, self.rate, self.am_BTC)
			
			i = 0
			s2 = ""
			exist = True
			
			while i<len(file_data):
				count = 0
				if file_data[i:i+4] == "2018":
					while count != 3:
						if file_data[i] == ".":
							count+=1
						if count != 3:
							s2 += file_data[i]
						else:
							s2 += file_data[i:i+9]
						i+=1
					
				if s2 == s:
					exist = False
					
				s2 = ""
				i+=1
			
			if exist:
				fo.write(s)
				fo.write("\n\n")
				print "%s Found a 1>BTC buy" % (self.date)
			
			fo.write(file_data)	
			fo.close()
		
			
		os.chdir("/Users/Max/Desktop/CRYPTO/Poloniex")
		
	
	def WriteSell(self):
	
		os.chdir("/Users/Max/Desktop/CRYPTO/Poloniex/TradeHistory")
		
		
		if not os.path.exists("/Users/Max/Desktop/CRYPTO/Poloniex/TradeHistory/" + self.Currency):
   			os.makedirs("/Users/Max/Desktop/CRYPTO/Poloniex/TradeHistory/" + self.Currency)
   			
   		os.chdir("/Users/Max/Desktop/CRYPTO/Poloniex/TradeHistory/" + self.Currency)
   			
		name = self.Currency + "_Sells.txt"

		if self.am_BTC > 1:
			fo = open(name, "a+")
			fo.seek(0,0)
			file_data = fo.read()
			fo.seek(0,0)
			fo.truncate()
			
			s = "%s %s %d %.8f %.8f %.8f" % (self.date, self.Currency, self.globalTradeID, self.amount, self.rate, self.am_BTC)
			
			i = 0
			s2 = ""
			exist = True
			
			while i<len(file_data):
				count = 0
				if file_data[i:i+4] == "2018":
					while count != 3:
						if file_data[i] == ".":
							count+=1
						if count != 3:
							s2 += file_data[i]
						else:
							s2 += file_data[i:i+9]
						i+=1
					
				if s2 == s:
					exist = False
					
				s2 = ""
				i+=1
			
			if exist:
				fo.write(s)
				fo.write("\n\n")
				print "%s Found a 1>BTC sell" % (self.date)
				
			fo.write(file_data)
			fo.close()
		
			
		os.chdir("/Users/Max/Desktop/CRYPTO/Poloniex")
		
def parser(string,name):
	
	i = 0
	n_name = ""
	
	while i<len(name):
		if name[i] == '_':
			n_name += name[i+1:i+5]
		i+=1
	
	name = n_name
	
	Book = TradeBook()
	Book2 = TradeBook()
	BookM = TradeBook()
	BookMB = TradeBook()
	BookMS = TradeBook()
	
	i = 0
	
	while i<len(string):
		
		if string[i:i+7] == "tradeID":
			i+=10
			tradeID = string[i:i+7]
			i+=10
		if string[i:i+6] == "amount":
			i+=11
			amount = string[i:i+10]
			i+=13
		if string[i:i+4] == "rate":
			i+=9
			rate = string[i:i+10]
			i+=15
		if string[i:i+4] == "date":
			i+=9
			date = string[i:i+19]
			i+=24
		if string[i:i+5] == "total":
			i+=10
			total = string[i:i+10]
			i+=15
		if string[i:i+4] == "type":
			i+=9
			if string[i] == 'b':
				type = string[i:i+3]
				i+=8
			else:
				type = string[i:i+4]
				i+=9
		if string[i:i+13] == "globalTradeID":
			i+=16
			
			globalTradeID = string[i:i+9]
			
			Book = TradeBook()
			Book2 = TradeBook()
			
			
			if type == "buy":
				Book.Currency = name
				Book.tradeID = int(tradeID)
				Book.type = type
				Book.amount = float(amount)
				Book.rate = float(rate)
				Book.am_BTC = Book.amount * Book.rate
				Book.date = date
				Book.globalTradeID = int(globalTradeID)
				Book.WriteBuy()
			else:
				Book2.Currency = name
				Book2.tradeID = int(tradeID)
				Book2.type = type
				Book2.amount = float(amount)
				Book2.rate = float(rate)
				Book2.am_BTC = Book2.amount * Book2.rate
				Book2.date = date
				Book2.globalTradeID = int(globalTradeID)
				Book2.WriteSell()
				
			'''if Book.amount != 0.0:
				BookM.Market(Book)
				BookMB.Market(Book)
			if Book2.amount != 0.0:
				BookM.Market(Book2)
				BookMS.Market(Book2)'''
			
			del Book
			del Book2
			i+=15
		i+=1
	
	'''BookM.PrintMBook()
	BookMB.PrintMBook()
	BookMS.PrintMBook()
	
	del BookMB
	del BookMS 
	del BookM'''



		
