'''
Return True if the string "cat" and "dog" appear the same number of times in the given string.

cat_dog('catdog') --> True
cat_dog('catcat') --> False
cat_dog('1cat1cadodog') --> True
'''
def catDog(string):
	if string.count('dog') == 0 or string.count('cat') == 0:
		print('{} --> false'.format(string))
	elif string.count('dog') != string.count('cat'):
		print('{} --> false'.format(string))
	else:
		print('{} --> true'.format(string))
catDog('Roscoecatdogcatdog P. Coltrane')
catDog('Roscoe P. Coltrane')
catDog('Roscoecatdogcat P. Coltrane')
