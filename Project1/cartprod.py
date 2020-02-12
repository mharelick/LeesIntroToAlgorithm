
'''
func cartprod(A,B)
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
   print (str(A))
   print (str(B))
   for itemA in A:
      '''for each item b in B'''
      for itemB in B:
         '''create a tuple (a,b ) called pair'''
         pair = [itemA,itemB]
         '''add pair to combinedList'''
         combinedList.append(pair)
    #return combinedList
   return combinedList


def TestCartPair1():
	leftside = ['a','b','c']
	rightside = [1,2,3,4,5]
	prod = cartprod(leftside, rightside)
	assert(len(prod) == len(leftside) * len(rightside))
	print (str(prod))
def TestZeroLengthLists():
	leftside = None
	rightSide = ['1',2,4,4]
	prod = cartprod(leftside,rightside)
	assert (0 == len(prod))
	prod = cartprod(rightside, leftside)
	assert ( 0 == len(prod))
	leftside = []
	prod = cartprod(leftside, righside)
	assert(0 == len(prod))
	prod = cartprod(rightside, leftside	)
	assert( 0 == len(prod))
	prod = cartprod([],[])
	assert( 0 == len(prod))
	prod = cartprod(None,None)
	assert ( 0 == len(prod))

def Main():
	TestCartPair1()
if __name__ == '__main__':
	Main()
