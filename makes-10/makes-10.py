a = ''
b = ''

print('MAKES 10\n--------\nDo the two numbers given either:\n     a) add to make 10, or…\n     b) are one or the other or\n        both numbers 10?\n')

def makes10(a,b):
	if a + b == 10 or a == 10 or b == 10:
		print('{} and {} checks out as true!'.format(a,b))
	else:
		print('{} and {} checks out as false!'.format(a,b))

makes10(5,4)
makes10(10,1)
makes10(1,9)
makes10(6,6)
makes10(7,2)
makes10(1,10)
makes10(10,10)
makes10(0,0)
makes10(-12,22)
makes10(-10,-10)
makes10(100,-90)
