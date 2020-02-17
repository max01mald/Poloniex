
class Bundle:
	array = []
	array2 = []
	
	def __init__(self, array, array2):
		self.array = array
		self.array2 = array2
		
def QuickSort(array, array2):
	bundle = Bundle(array, array2)
	return QuickSortB(bundle)
	
def QuickSortB(bundle):
	
	loc = len(bundle.array)/2
	pivot = bundle.array[loc]
	pivot2 = bundle.array2[loc]
	
	small = []
	small2 =[]
	big = []
	big2 = []
	bundleS = Bundle([],[])
	bundleB = Bundle([],[])
	
	if len(bundle.array) == 1:
		return bundle
	
	i=0
	
	while i<len(bundle.array):
		if bundle.array[i] < pivot:
			small.append(bundle.array[i])
			small2.append(bundle.array2[i])
		if bundle.array[i] > pivot:
			big.append(bundle.array[i])
			big2.append(bundle.array2[i])
		i+=1

	bs = Bundle(small, small2)
	
	bb = Bundle(big, big2)
	
	
	if len(bs.array) != 0:
		bundleS = QuickSortB(bs)
	if len(bb.array) != 0:
		bundleB = QuickSortB(bb)
	
	bundle.array = bundleS.array + [pivot]
	bundle.array = bundle.array + bundleB.array
	
	bundle.array2 = bundleS.array2 + [pivot2]
	bundle.array2 = bundle.array2 + bundleB.array2
	
	return bundle
	
	
'''array = [2,4,5,1,3,8,6,10,9,7]
array2 = [1,2,3,4,5,6,7,8,9,10]

bundlem = QuickSort(array, array2)

print bundlem.array
print bundlemm.array2'''
	
		