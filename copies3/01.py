'''
Given a list of strings, return a list where each string is replaced by 3 copies of the string concatenated together.

copies3(["a", "bb", "ccc"]) ---> ["aaa", "bbbbbb", "ccccccccc"]
copies3(["24", "a", ""]) ---> ["242424", "aaa", ""]
copies3(["hello", "there"]) ---> ["hellohellohello", "theretherethere"]
'''
def copies3(theList):
    theListXiii = []
    for i in theList:
        i = i * 3
        theListXiii.append(i)
    print('{} ---> {}'.format(theList, theListXiii))
copies3(['Joe','Leah','Tommy'])
copies3(['x','H','Oh Yeah! '])
