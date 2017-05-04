'''
Given a string, if the string "del" appears starting at index 1, return a string where that "del" has been deleted. Otherwise, return the string unchanged.

delDel("adelbc") --> "abc"
delDel("adelHello") --> "aHello"
delDel("adedbc") --> "adedbc"
'''
def delDELETED(string):
	print('{} ---> {}'.format(string, string.replace('del', '')))
delDELETED('adelbc')
delDELETED('adelHello')
delDELETED('adedbc')
