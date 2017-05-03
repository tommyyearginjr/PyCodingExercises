'''
We'll say that a 1 immediately followed by a 3 in an array is an "unlucky" 1. Return true if the given array contains an unlucky 1 in the first 2 or last 2 positions in the array.

unlucky1([1, 3, 4, 5]) ---> true
unlucky1([2, 1, 3, 4, 5]) ---> true
unlucky1([1, 1, 1]) ---> false
'''
def unluckyOne(overcomer):
    if (overcomer[0] == 1 and overcomer[1] == 3) or (overcomer[1] == 1 and overcomer[2] == 3) or (overcomer[-1] == 3 and overcomer[-2] == 1):
        print('{} --> TRUE! There is an unlucky 1!!'.format(overcomer))
    else:
        print('{} --> FALSE! There is not an unlucky 1!!'.format(overcomer))

unluckyOne([1,3,4,5,6,1,3,1])
unluckyOne([1, 3, 4, 5])
unluckyOne([2, 1, 3, 4, 5])
unluckyOne([1, 1, 1])
unluckyOne([5,4,3,2,3,1,3])
# unluckyOne()
