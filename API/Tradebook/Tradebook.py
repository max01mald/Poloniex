import os
import time
import datetime
from Algorithms.QuickSort import QuickSort

class Book:
	Type = ""
	Id = ""
	Date = ""
	Currency = ""
	Price = []
	Quantity = []
	Sum = []
	
	
	def __init__(self):
		self.Type = ""
                self.Id = ""
                self.Date = "{:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now()) + ""
	        self.Currency = ""
                self.Price = []
                self.Quantity = []
                self.Sum = []

	def __del__(self):
		#print("delete")
		self.Type = ""
		self.Id = ""
		self.Date = ""
		self.Currency = ""
		del self.Price[:]
		del self.Quantity[:]
		del self.Sum[:]
	
	def printBook(self):
		print()
		print(self.Type)
		print(self.Id)
		print(self.Date)
		print(self.Currency)
		print()
		print("PRICES ----- QUANTITY ----- SUM")
		
		i=1
		while i<len(self.Price):
			print("%.8f %.8f %.8f" %(float(self.Price[i]), float(self.Quantity[i]), float(self.Sum[i])))
			i+=1
			
	def writeBook(self):
            
            if not os.path.exists(os.path.dirname(os.path.realpath(__file__)) + self.Currency):
                os.makedirs(os.path.dirname(os.path.realpath(__file__)) + self.Currency)

            os.chdir(os.path.dirname(os.path.realpath(__file__)))

            if not os.path.exists(os.path.dirname(os.path.realpath(__file__)) + self.Currency):
                os.makedirs(os.path.dirname(os.path.realpath(__file__)) + self.Currency)

            os.chdir(os.path.dirname(os.path.realpath(__file__)) + self.Currency)

            name = self.Type + ".txt"
            header = self.Date + " -- PRICES -- QUANTITY -- SUM\n"
	    fo = open(name, "a+")
	   
            fo.seek(0,0)
            file_data = fo.read()
            fo.seek(0,0)
            fo.truncate()

            if(len(file_data) != 0):
                file_data = file_data[len(header):]

            fo.write(header)

	    i=1
	    while i<len(self.Price):
	    	fo.write("%.8f %.8f %.8f\n" %(float(self.Price[i]), float(self.Quantity[i]), float(self.Sum[i])))
	    	i+=1
	    
	    fo.close
    
		
def parser(string, pair):
	
	book = Book()
	book2 = Book()
	
	i = 0
        while i<len(pair):
                if pair[i] == '_':
			book.Currency = pair[i+1:]
			book2.Currency = pair[i+1:]
		i+=1
	i=0
	
	section = 0 
	while i<len(string):
		if string[i] == "b":
			section = 1
			book.Type = string[i:i+3]
		if string[i] == 'a':
			section  = 2
			book2.Type = string[i:i+3]
		if string[i] == 'u':
			j=0
			pr = ""
			qu = ""
			while j != 5:
				if string[i+2] == 's' or string[i+2] == 'a' or string[i+2] == 'b':
					j = 5
				if string[i] == '\'' or string[i] == ',' or string[i] == ']':
					j += 1
					if string[i] == '\'':
						if j == 1:
							i+=1
					if string[i] == ',':
						if j == 3:
							i+=1

				if j == 1:
					pr += string[i]
				if j == 3:
					qu += string[i]
				if j == 4:
					if section == 1:
						book.Price.append(float(pr))
						book.Quantity.append(float(pr)*float(qu))
						j+=1
					if section == 2:
						book2.Price.append(float(pr))
						book2.Quantity.append(float(pr)*float(qu)) 
						j+=1
				i+=1
				
		if string[i] == 's':
			j = i+6
                        while string[j] != "}":
                            j+=1
                        book.Id = string[i+6:j]
			book2.Id = string[i+6:j]
		i+=1
		
	sort1 = QuickSort(book.Price, book.Quantity)
	sort2 = QuickSort(book2.Price, book2.Quantity)
	
	book.Price = sort1.array
	book.Quantity = sort1.array2
	
	book2.Price = sort2.array
	book2.Quantity = sort2.array2
	
	i=0
	sum = 0
	sum2 = 0
	while i<len(book.Quantity):
		sum += float(book.Quantity[i])
		sum2 += float(book2.Quantity[i])
		
		book.Sum = book.Sum + [sum]
		book2.Sum = book2.Sum + [sum2]
		i+=1
		
	'''		
	book.printBook()
	book2.printBook()
        '''
	
	book.writeBook()
        book2.writeBook()
	
	del book
	del book2
	

