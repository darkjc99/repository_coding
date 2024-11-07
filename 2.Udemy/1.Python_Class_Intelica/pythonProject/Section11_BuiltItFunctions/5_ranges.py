import sys


#numbers: range = range(0,-10,-3)
#print(list(numbers))

numbers: range = range(10**20)
print(sys.getsizeof(numbers))
