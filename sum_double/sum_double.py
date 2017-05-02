'''
Given two int values, return their sum. Unless the two values are the same, then return double their sum.

Examples:
sum_double(1, 2) → 3
sum_double(3, 2) → 5
sum_double(2, 2) → 8
'''
def DubbaSum(a,b):
	if a == b:
		print('({} + {}) X 2 = {}'.format(a,b,((a+b)*2)))
	else:
		print('{} + {} = {}'.format(a,b,a+b))

DubbaSum(3,2)
DubbaSum(4,4)
DubbaSum(6,7)
DubbaSum(10,10)
