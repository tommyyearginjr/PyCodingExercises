'''
Given a string, take the last char and return a new string with the last char added at the front and back, so "cat" yields "tcatt". The original string will be length 1 or more.

backAround("cat") --> "tcatt"
backAround("Hello") --> "oHelloo"
backAround("a") --> "aaa"
'''
def back_around(string):
	charList = list()
	for i in string:
		charList.append(i)
	print('{} ---> {}'.format(string, charList[-1]+string+charList[-1]))
back_around('cat')
back_around('Hello')
back_around('a')
