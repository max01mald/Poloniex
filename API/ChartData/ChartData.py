import os
import time
import datetime

class ChartData:
    Currency = ""
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
	self.Currency = ""
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
        self.Currency = ""
	self.Volume = 0.0
	self.QuoteVolume = 0.0
	self.High = 0.0
	self.Low = 0.0
        self.Date = 0
	self.Close = 0.0
	self.WeightedAverage = 0.0
	self.Open = 0.0
	del self.Market[:]
    
    def PrintChart(self):
        print() 
        print(self.Currency)
        print(self.Date)
        print(self.Volume)
        print(self.QuoteVolume)
        print(self.High)
        print(self.Low)
        print(self.Open)
        print(self.Close)
        print(self.WeightedAverage)
        print()

    def WriteC(self, lapse):

        if not os.path.exists(os.path.dirname(os.path.realpath(__file__)) + "/ChartData/"):
            os.makedirs(os.path.dirname(os.path.realpath(__file__)) + "/ChartData/")

        os.chdir(os.path.dirname(os.path.realpath(__file__)) + "/ChartData/")

        if not os.path.exists(os.path.dirname(os.path.realpath(__file__)) + "/ChartData/" + self.Currency):
            os.makedirs(os.path.dirname(os.path.realpath(__file__)) + "/ChartData/" + self.Currency)
                        
        os.chdir(os.path.dirname(os.path.realpath(__file__)) + "/ChartData/" + self.Currency)
        
        name = str(int(lapse)/60)+"min_Chart.txt"
        header = "DATE -- HIGH -- LOW -- OPEN -- CLOSE -- VOLUME -- QUOTE_VOLUME -- WEIGHTED_AVERAGE \n"

        fo = open(name, "a+")
        fo.seek(0,0)
        file_data = fo.read()
        fo.seek(0,0)
        fo.truncate()

        top = True
        if(len(file_data) != 0):
            file_data = file_data[len(header):]
            top_date = time.mktime(datetime.datetime.strptime(file_data[0:19],"%Y-%m-%d %H:%M:%S").timetuple())
            incoming_date = time.mktime(datetime.datetime.strptime(self.Date,"%Y-%m-%d %H:%M:%S").timetuple())
            if incoming_date - top_date <= 0:
                top = False

        fo.write(header)

        if top:
            fo.write("%s %.8f %.8f %.8f %.8f %.8f %.8f %.8f\n"
                                % (self.Date, self.High, self.Low, self.Open, self.Close, self.Volume,
                                   self.QuoteVolume, self.WeightedAverage))

        fo.write(file_data)
        fo.close()

        os.chdir(os.path.dirname(os.path.realpath(__file__)) + "/Ticker")

        os.chdir(os.path.dirname(os.path.realpath(__file__)))



def parser(string, pair, lapse):
	
	i=0
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
		    i+=4
                
                Chart = ChartData()
                Chart.Currency = pair
                Chart.Volume = float(Volume)
                Chart.QuoteVolume = float(QuoteVolume)
                Chart.High = float(High)
                Chart.Low = float(Low)
                Chart.Date = str(datetime.datetime.fromtimestamp(float(Date)))
                Chart.Close = float(Close)
                Chart.WeightedAverage = float(WeightedAverage)
                Chart.Open = float(Open)
                
                #Chart.PrintChart()
                Chart.WriteC(lapse)
            i+=1
	
