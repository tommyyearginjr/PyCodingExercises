'''
Given a list of integers, return a list where each integer is multiplied by 2.

doubling([1, 2, 3]) --> [2, 4, 6]
doubling([6, 8, 6, 8, -1]) --> [12, 16, 12, 16, -2]
'''
def doubling(theList):
    doubleList = []
    for i in theList:
        i = i * 2
        doubleList.append(i)
    print('{} --> {}'.format(theList, doubleList))
doubling([1,2,3])
doubling([7,8,9])
