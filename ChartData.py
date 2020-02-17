
class ChartData:
	Volume = 0.0
	QuoteVolume = 0.0
	High = 0.0
	Low = 0.0
	Date = 0
	Close = 0.0
	WeightedAverage = 0.0
	Open = 0.0
	Market = []
	
	def __init__(self):
		self.Volume = 0.0
		self.QuoteVolume = 0.0
		self.High = 0.0
		self.Low = 0.0
		self.Date = 0
		self.Close = 0.0
		self.WeightedAverage = 0.0
		self.Open = 0.0
		self.Market = []
		
	def __del__(self):
		self.Volume = 0.0
		self.QuoteVolume = 0.0
		self.High = 0.0
		self.Low = 0.0
		self.Date = 0
		self.Close = 0.0
		self.WeightedAverage = 0.0
		self.Open = 0.0
		del self.Market[:]
		
def parser(string):
	
	i=0
	
	print string
	
	while i<len(string):

		if string[i:i+6] == "volume":
			i+=9
			j =0
			Volume = ""
			while j<2:
				if string[i] == "." or string[i] == ",":
					j+=1
				if j<2:
					Volume += string[i]
					i+=1
			i+=4
		
		if string[i:i+11] == 'quoteVolume':
			i+=15
			j =0
			QuoteVolume = ""
			while j<2:
				if string[i] == "." or string[i] == ",":
					j+=1
				if j<2:
					QuoteVolume += string[i]
					i+=1
			i+=4
			
		if string[i:i+4] == "high":
			i+=7
			j =0
			High = ""
			while j<2:
				if string[i] == "." or string[i] == ",":
					j+=1
				if j<2:
					High += string[i]
					i+=1
			i+=4
		
		if string[i:i+3] == "low":
			i+=6
			j =0
			Low = ""
			while j<2:
				if string[i] == "." or string[i] == ",":
					j+=1
				if j<2:
					Low += string[i]
					i+=1
			i+=4
		
		if string[i:i+4] == "date":
			i+=7
			Date = string[i:i+10]
			i+= 14
		
		if string[i:i+5] == "close":
			i+=8
			j =0
			Close = ""
			while j<2:
				if string[i] == "." or string[i] == ",":
					j+=1
				if j<2:
					Close += string[i]
					i+=1
			i+=4
		
		if string[i:i+15] == "weightedAverage":
			i+=18
			j =0
			WeightedAverage = ""
			while j<2:
				if string[i] == "." or string[i] == ",":
					j+=1
				if j<2:
					WeightedAverage += string[i]
					i+=1
			i+=4
		
		if string[i:i+4] == "open":
			i+=7
			j =0
			Open = ""
			while j<2:
				if string[i] == "." or string[i] == "}":
					j+=1
				if j<2:
					Open += string[i]
					i+=1
			print Open
			i+=4
			
			
		
		i+=1
	
