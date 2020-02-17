

class QueuePol:
	array = [None]
	front = 0
	end = 1
	sum = 0
	fill = 0.0
	m_avg = 0
	
	
	
	def __init__(self, number):
		self.array = [None]*number
		
	def dequeue(self):
		if self.array[self.front] is None:
			print "Queue is Empty"
		else:
			self.sum -= self.array[self.front]
			self.array[self.front] = None
			self.fill -= 1
			self.front = (self.front + 1)%len(self.array)
			

	def enqueue(self, value):
		i = 0
		while i<len(self.array):
			if self.array[i] is None:
				self.array[i] = value
				self.fill += 1
				self.sum += value
				self.calc_avg(self.fill,self.sum)
				
				if i+1 != len(self.array):
					self.end = i+1
					return
					
			elif i == len(self.array)-1:
				self.dequeue()
				self.end = self.front-1 
				self.array[self.end] = value
				self.fill += 1
				self.sum += value
				self.calc_avg(self.fill,self.sum)
				return
				
			i += 1
	
	def get(self, i):
		return self.array[i]
		
	def calc_avg(self, fills, sums):
		#print sums
		#print fills
		self.m_avg = sums/fills
		
	def printA(self):
		i=0
		while i<len(self.array):
			#print self.get(i) 
			i += 1
	
	
			


'''queue = QueuePol(5)

i=0
while i<10000:
	queue.enqueue(i)
	
	print queue.m_avg 
	i += 1 '''
