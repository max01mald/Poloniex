import os
import sys
import time
import datetime


class Ticker:
    Date = ""
    Currency = ""
    Last = 0.0
    QuoteVolume = 0.0
    High24hr = 0.0
    isFrozen = 0
    HighestBid = 0.0
    PercentChange = 0.0
    Low24hr = 0.0
    LowestAsk = 0.0
    ID = 0
    BaseVolume = 0.0
    Market = []


    def __init__(self):
        self.Date = "{:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now())
        self.Currency = ""
        self.Last = 0.0
        self.QuoteVolume = 0.0
        self.High24hr = 0.0
        self.isFrozen = 0
        self.HighestBid = 0.0
        self.PercentChange = 0.0
        self.Low24hr = 0.0
        self.LowestAsk = 0.0
        self.ID = 0
        self.BaseVolume = 0.0
        self.Market = []


    def __del__(self):
        self.Date = ""
        self.Currency = ""
        self.Last = 0.0
        self.QuoteVolume = 0.0
        self.High24hr = 0.0
        self.isFrozen = 0
        self.HighestBid = 0.0
        self.PercentChange = 0.0
        self.Low24hr = 0.0
        self.LowestAsk = 0.0
        self.ID = 0
        self.BaseVolume = 0.0
        del self.Market[:]


    def PrinT(self):
        print("%s %.8f %.8f %.8f %d %.8f %.8f %.8f %.8f %d %.8f" % \
        (self.Currency, self.Last, self.QuoteVolume, self.High24hr
        , self.isFrozen, self.HighestBid, self.PercentChange, self.Low24hr
        , self.LowestAsk, self.ID, self.BaseVolume))


    def PrintM(self):
        for market in self.Market:
            market.PrinT()


    def WriteM(self):
        os.chdir(os.path.dirname(os.path.realpath(__file__)) + "/Ticker")

        for market in self.Market:
            if not os.path.exists(os.path.dirname(os.path.realpath(__file__)) + "/Ticker/" + market.Currency):
                os.makedirs(os.path.dirname(os.path.realpath(__file__)) + "/Ticker/" + market.Currency)

            os.chdir(os.path.dirname(os.path.realpath(__file__)) + "/Ticker/" + market.Currency)

            name = "Ticker.txt"
            header = "DATE -- CURRENCY -- LAST -- QUOTE_VOLUME -- PER_CHG -- 24_HIGH -- 24_LOW -- HIGH_BID -- LOW_ASK -- BASE_VOLUME - ID - F -\n"

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
                fo.write("%s %s %.8f %.8f %.8f %.8f %.8f %.8f %.8f %.8f %d %d\n"
                    % (market.Date, market.Currency, market.Last, market.QuoteVolume, market.PercentChange
                    , market.High24hr, market.Low24hr, market.HighestBid, market.LowestAsk
                    , market.BaseVolume, market.ID, market.isFrozen))

            fo.write(file_data)
            fo.close()

            os.chdir(os.path.dirname(os.path.realpath(__file__)) + "/Ticker")

        os.chdir(os.path.dirname(os.path.realpath(__file__)))


    def ReadM(self, pair):
        name = "Ticker.txt"
        os.chdir(os.path.dirname(os.path.realpath(__file__)) + "/Ticker/" + pair)

        fo = open(name, "r")
        fo.seek(0,0)

        # Drop Header
        fo.readline()

        for line in fo:
            line_data = fo.readline()
            data_tokens = line_data.split()

            if(len(data_tokens) < 13):
                break

            self.Date = data_tokens[0] + data_tokens[1]
            self.Currency = data_tokens[2]
            self.Last = float(data_tokens[3])
            self.QuoteVolume = float(data_tokens[4])
            self.PercentChange = float(data_tokens[5])
            self.High24hr = float(data_tokens[6])
            self.Low24hr = float(data_tokens[7])
            self.HighestBid = float(data_tokens[8])
            self.LowestAsk = float(data_tokens[9])
            self.BaseVolume = float(data_tokens[10])
            self.ID = int(data_tokens[11])
            self.isFrozen = int(data_tokens[12])

            self.Market.append(self)


    def GetSentiment(self):
        day_span = self.Market[0].High24hr - self.Market[0].Low24hr
        day_perc = day_span / self.Market[0].Low24hr * 100

        print(day_span)
        print(day_perc)

        for trade in self.Market:
            buy_span = trade.LowestAsk - trade.HighestBid
            buy_perc = buy_span / trade.HighestBid * 100            
            print("%.8f %.8f" %(buy_span, buy_perc))


def parser(string):

    i=0
    BTC_Market = Ticker()
    ETH_Market = Ticker()
    USDT_Market = Ticker()
    XMR_Market = Ticker()

    while i<len(string):

        if string[i] == '_':
            Cuerrency = ""
            j = i-3
            while string[j] != "'":
                j+=1
            if string[i-4] != "'":
                Currency = string[i-4:j]
            else:
                Currency = string[i-3:j]

            i+=9

        if string[i:i+4] == "last":
            i+=9
            Last = string[i:i+10]
            i+=15

        if string[i:i+11] == "quoteVolume":
            i+=17
            j=0
            QuoteVolume = ""
            while j<2:
                if string[i] == '.' or string[i] == "'":
                    j +=1
                if j<2:
                    QuoteVolume += string[i]
                    i+=1
            i+=5

        if string[i:i+8] == "high24hr":
            i+=13
            j=0
            High24hr = ""
            while j<2:
                if string[i] == '.' or string[i] == "'":
                    j +=1
                if j<2:
                    High24hr += string[i]
                    i+=1
            i+=5

        if string[i:i+8] == "isFrozen":
            i+= 13
            isFrozen = string[i]
            i+=6

        if string[i:i+10] == "highestBid":
            i+=15
            j=0
            HighestBid = ""
            while j<2:
                if string[i] == '.' or string[i] == "'":
                    j +=1
                if j<2:
                    HighestBid += string[i]
                    i+=1
            i+=5

        if string[i:i+13] == "percentChange":
            i+=18
            j=0
            PercentChange = ""
            while j<2:
                if string[i] == '.' or string[i] == "'":
                    j +=1
                if j<2:
                    PercentChange += string[i]
                    i+=1
            i+=5

        if string[i:i+7] == "low24hr":
            i+=12
            j=0
            Low24hr = ""
            while j<2:
                if string[i] == '.' or string[i] == "'":
                    j +=1
                if j<2:
                    Low24hr += string[i]
                    i+=1
            i+=5

        if string[i:i+9] == "lowestAsk":
            i+= 14
            j=0
            LowestAsk = ""
            while j<2:
                if string[i] == '.' or string[i] == "'":
                    j +=1
                if j<2:
                    LowestAsk += string[i]
                    i+=1
            i+=5
        if string[i:i+2] == "id":
            i+=5
            j=0
            ID = ""
            while j<1:
                if string[i] == ',':
                    j +=1
                if j<1:
                    ID += string[i]
                    i+=1
            i+=4

        if string[i:i+10] == "baseVolume":
            i+=15
            j=0
            BaseVolume = ""
            j=0
            BaseVolume = ""
            while j<2:
                if string[i] == '.' or string[i] == "'":
                    j +=1
                if j<2:
                    BaseVolume += string[i]
                    i+=1

            k = 0


            while k<len(Currency):
                if Currency[k] == '_':
                    size = k
                k+=1

            if Currency[0:size] == "BTC":

                BTC = Ticker()

                BTC.Currency = Currency
                BTC.Last = float(Last)
                BTC.QuoteVolume = float(QuoteVolume)
                BTC.High24hr = float(High24hr)
                BTC.isFrozen = int(isFrozen)
                BTC.HighestBid = float(HighestBid)
                BTC.PercentChange = float(PercentChange)
                BTC.Low24hr = float(Low24hr)
                BTC.LowestAsk = float(LowestAsk)
                BTC.ID = int(ID)
                BTC.BaseVolume = float(BaseVolume)
                BTC_Market.Market = BTC_Market.Market + [BTC]
                del BTC

            if Currency[0:size] == "ETH":

                ETH = Ticker()

                ETH.Currency = Currency
                ETH.Last = float(Last)
                ETH.QuoteVolume = float(QuoteVolume)
                ETH.High24hr = float(High24hr)
                ETH.isFrozen = int(isFrozen)
                ETH.HighestBid = float(HighestBid)
                ETH.PercentChange = float(PercentChange)
                ETH.Low24hr = float(Low24hr)
                ETH.LowestAsk = float(LowestAsk)
                ETH.ID = int(ID)
                ETH.BaseVolume = float(BaseVolume)

                ETH_Market.Market = ETH_Market.Market + [ETH]
                del ETH

            if Currency[0:size] == "USDT":

                USDT = Ticker()

                USDT.Currency = Currency
                USDT.Last = float(Last)
                USDT.QuoteVolume = float(QuoteVolume)
                USDT.High24hr = float(High24hr)
                USDT.isFrozen = int(isFrozen)
                USDT.HighestBid = float(HighestBid)
                USDT.PercentChange = float(PercentChange)
                USDT.Low24hr = float(Low24hr)
                USDT.LowestAsk = float(LowestAsk)
                USDT.ID = int(ID)
                USDT.BaseVolume = float(BaseVolume)

                USDT_Market.Market = USDT_Market.Market + [USDT]
                del USDT

            if Currency[0:size] == "XMR":

                XMR = Ticker()

                XMR.Currency = Currency
                XMR.Last = float(Last)
                XMR.QuoteVolume = float(QuoteVolume)
                XMR.High24hr = float(High24hr)
                XMR.isFrozen = int(isFrozen)
                XMR.HighestBid = float(HighestBid)
                XMR.PercentChange = float(PercentChange)
                XMR.Low24hr = float(Low24hr)
                XMR.LowestAsk = float(LowestAsk)
                XMR.ID = int(ID)
                XMR.BaseVolume = float(BaseVolume)

                XMR_Market.Market = XMR_Market.Market + [XMR]
                del XMR


        i+=1

    #BTC_Market.PrintM()
    BTC_Market.WriteM()
    #ETH_Market.PrintM()
    #USDT_Market.PrintM()
    #XMR_Market.PrintM()

    del BTC_Market
    del ETH_Market
    del USDT_Market
    del XMR_Market
