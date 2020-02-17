


def priceTicker(string):
	i=1
	price = ""
	temp = "" 
	while i<len(string):
		if string[-i] != " ":
			price = string[-i] + price
		
			i += 1
		else:
			return price
				

			

	
	
