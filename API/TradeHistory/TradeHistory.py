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
		print("%s %s %.8f %.8f %.8f" % (self.Currency, self.type, self.rate, self.amount, self.am_BTC))
	
	def PrintMBook(self):
		
		i=0
		
		while i<len(self.Trades):
			self.Trades[i].PrintBook()
			i+=1

	def Market(self, Book):
			NBook = Book.Copy()
			self.Trades = self.Trades + [NBook]
			
	def WriteBuy(self):
	    		
	    if not os.path.exists(os.path.dirname(os.path.realpath(__file__)) + self.Currency):
   	    	os.makedirs(os.path.dirname(os.path.realpath(__file__)) + self.Currency)
   			
   	    os.chdir(os.path.dirname(os.path.realpath(__file__)) + self.Currency)
   			
	    name = "Buys.txt"
			
	    if self.am_BTC > 1:
		fo = open(name, "a+")
		fo.seek(0,0)
		file_data = fo.read()
		fo.seek(0,0)
		fo.truncate()

                header = "DATE -- CURRENCY -- TRADE_ID -- AMOUNT -- RATE -- SUM_BTC\n" 
		s = "%s %s %d %.8f %.8f %.8f" % (self.date, self.Currency, self.globalTradeID, self.amount, self.rate, self.am_BTC)
	        		
                if(len(file_data) != 0):
                    file_data = file_data[len(header):]

		beg = 0
                end = beg
		s2 = ""
		exist = True
		    
		while end <len(file_data):
		    
                    if file_data[end] == "\n":
                        s2 = file_data[beg:end]                        
                        beg = end + 1
	
		    if s2 == s:
			exist = False
                    
                    s2 = ""
		    end+=1
		
                fo.write(header)

		if exist:
		    fo.write(s)
		    fo.write("\n")
                    print("%s Found a 1>BTC buy" % (self.date))
			
		fo.write(file_data)	
		fo.close()
		
			
	    os.chdir(os.path.dirname(os.path.realpath(__file__)))
		
	
	def WriteSell(self):
		
	    if not os.path.exists(os.path.dirname(os.path.realpath(__file__)) + self.Currency):
   	    	os.makedirs(os.path.dirname(os.path.realpath(__file__)) + self.Currency)
   			
   	    os.chdir(os.path.dirname(os.path.realpath(__file__)) + self.Currency)
   			
	    name = "Sells.txt"

	    if self.am_BTC > 1:
                fo = open(name, "a+")
		fo.seek(0,0)
		file_data = fo.read()
		fo.seek(0,0)
		fo.truncate()
			
		header = "DATE -- CURRENCY -- TRADE_ID -- AMOUNT -- RATE -- SUM_BTC\n"
                s = "%s %s %d %.8f %.8f %.8f" % (self.date, self.Currency, self.globalTradeID, self.amount, self.rate, self.am_BTC)

                if(len(file_data) != 0):
                    file_data = file_data[len(header):]

                beg = 0
                end = beg

		s2 = ""
		exist = True
			
		while end<len(file_data):

                    if file_data[end] == "\n":
                        s2 = file_data[beg:end]
                        beg = end + 1

                    if s2 == s:
                        exist = False
			       			
		    s2 = ""
		    end+=1
		
                fo.write(header)

		if exist:
		    fo.write(s)
		    fo.write("\n")
		    print("%s Found a 1>BTC sell" % (self.date))		
		    
                fo.write(file_data)
		fo.close()
		
			
	    os.chdir(os.path.dirname(os.path.realpath(__file__)))
		
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
                        j = i
                        while string[j] != ",":
                            j+=1
			tradeID = string[i:j]
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
				
			if Book.amount != 0.0:
				BookM.Market(Book)
				BookMB.Market(Book)
			if Book2.amount != 0.0:
				BookM.Market(Book2)
				BookMS.Market(Book2)
			
			del Book
			del Book2
			i+=15
		i+=1
	
        BookMB.WriteBuy()
        BookMS.WriteSell()
	#BookM.PrintMBook()
        #BookMB.PrintMBook()
        #BookMS.PrintMBook()
	
	del BookMB
	del BookMS 
	del BookM



		
