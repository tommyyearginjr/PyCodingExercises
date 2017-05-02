'''
Given a non-negative int n, return the count of the occurrences of 7 as a digit, so for example 717 yields 2. (no loops). Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).

Examples:
count7(717) --> 2
count7(7) --> 1
count7(123) --> 0

***********************
* NOTE:               *
* print(717%10) >> 7  *
* print(717/10) >> 71 *
***********************
'''

from collections import Counter

def count7(x):
    if x < 0:
        print('\'{}\' will be converted to the positive integer \'{}\'!'.format(x, x*-1))
        x = x * -1
    x = str(x)
    counter = Counter(x)
    print('The number of occurrences of \'7\' in {} is {}.\n'.format(x,counter['7']))

count7(987)
count7(777771)
count7(123456890)
count7(-67)
