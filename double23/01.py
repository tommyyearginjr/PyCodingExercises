'''

Given an int array, return true if the array contains 2 twice, or 3 twice.

double23([2, 2]) --> true
double23([3, 3]) --> true
double23([2, 3]) --> false
'''

def DoubleTwoThree(BroStair):
    if BroStair.count(2) >= 2 or BroStair.count(3) >= 2:
        print('{} --> TRUE!'.format(BroStair))
    else:
        print('{} --> FALSE!'.format(BroStair))

DoubleTwoThree([2,2])
DoubleTwoThree([3,3])
DoubleTwoThree([2,3])
DoubleTwoThree([1,2,3,4,5,2,5,6,7,8,9,0])
