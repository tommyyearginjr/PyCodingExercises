'''
Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".

Examples:
string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello'
'''

def stringBits(string1):
	list1 = []
	list2 = []
	for i in string1:
		list1.append(i)
	for i in range(0, len(list1), 2):
		list2.append(list1[i])
	print('{} --> {}'.format(string1,''.join(list2)))

stringBits('xoxoxo')
stringBits('mesothelioma')
stringBits('tommyhyearginjr')
stringBits('Heeololeo')
