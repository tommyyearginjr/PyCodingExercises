'''
Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).

Examples:
last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2
'''
import re

def xlastxtwox(brick):
	list1 = []
	list1.append(re.findall('..',brick))
	beanBurger = list1[0][0]
	bbCount = list1[0].count(beanBurger)
	lastTwo = list1[0][-1]
	if lastTwo == beanBurger:
		print('String \'{}\' --> {}'.format(brick,bbCount - 1))
	else:
		print('String \'{}\' --> {}'.format(brick,bbCount))
		
xlastxtwox('stxxsstst')
xlastxtwox('momomofofomo')
xlastxtwox('ayxxayxxax')
xlastxtwox('pupulpufictionpu')
xlastxtwox('sesamestreetsesesa')
