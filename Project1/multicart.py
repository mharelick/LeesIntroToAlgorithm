'''N way cartesian product:
What can be determined at the function time: 
1. The number of sets
2. The size of each set
3. Each tuple consists of N elements
4. Repeats: Where will there be repeats?

A = [a,b,c]
B = [1,2,3]
C = [pear,apple]

So each tuple consists of three elements. 
a,1,pear
a,1,apple
a,2,pear
a,2,apple
a,3,pear
a,3,apple
a,
'''

def cartprod(A,B):

   '''combinedList = empty set'''
   combinedList = []
   '''if length of A is 0 or length of B is 0 return combinedList'''
   if A is None or B is None:
   	   return combinedList
   if 0 == len(A) or 0 == len(B):
   	   return combinedList
   '''for each item a in A'''
   
   for itemA in A:
      '''for each item b in B'''
      #print ( "Original list  {}".format(str(itemA)))
      for itemB in B:
         '''create a tuple (a,b ) called pair'''
         #print ( "New item   {}".format(str(itemB)))

         if type(itemA) is list:
         	pair = itemA.copy() # We want pair to be a separate copy rather than reference.
         	pair.append(itemB)
         else:
            pair = [itemA,itemB]
         '''add pair to combinedList'''
         combinedList.append(pair)
    #return combinedList
   return combinedList


def multicart1(items):
	if items is None:
		return []
	if len(items ) == 0:
		return []

	firstList = items[0]
	totalList = firstList
	print (str(totalList))
	for x in range(1,len(items)):
		
		totalList = cartprod(totalList, items[x])
		
		#print (totalList)
		if totalList == []:
			return []
		#print (totalList)
	return totalList



def TestPair():
	leftside = ['a','b','c']
	rightside = [1,2,3,4,5]
	prod = cartprod(leftside, rightside)
	assert(len(prod) == len(leftside) * len(rightside))
	print (str(prod))

def TestThree():
	letters = ['a','b','c']
	numbers = [1,2,3,4,5]
	fruits = ["pear","apple"]
	prod = multicart1([letters,numbers,fruits])
	assert (len(prod) == len(letters) * len(numbers) * len(fruits))
	print (str(prod))


def Main():
	TestPair()
	TestThree()


if __name__ == '__main__':
	Main()








