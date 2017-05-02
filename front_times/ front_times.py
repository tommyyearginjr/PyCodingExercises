'''
Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;

Examples:
front_times('Chocolate', 2) → 'ChoCho'
front_times('Chocolate', 3) → 'ChoChoCho'
front_times('Abc', 3) → 'AbcAbcAbc'
'''

def frontTimes(theString, theMultiplier):
	if theMultiplier < 0:
		theMultiplier = theMultiplier * -1
	theString_broken = []
	theInteger = 3
	SingPlur = 'The first {} letters'.format(theInteger)
	for i in theString:
		theString_broken.append(i)
	if len(theString_broken) <= theInteger:
		theInteger = len(theString_broken)
		SingPlur = '\'{}\''.format(theString)
	theString_reassembled = []
	for x in range(0, theInteger, 1):
		theString_reassembled.append(theString_broken[x])
	print('The given word is \'{}\'...\n{} X {} --> {}\n'.format(theString, SingPlur, theMultiplier, (''.join(theString_reassembled)) * theMultiplier))

frontTimes('Cruiser',-2)
frontTimes('Jamoni',5)
frontTimes('po',3)
frontTimes('PeeWee',-5)
frontTimes('I',-99)
frontTimes('by',9)
