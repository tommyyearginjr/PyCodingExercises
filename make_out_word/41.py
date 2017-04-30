MyBorder = ""
def makeoutword(MyBorder, MyString):
    charList = list()
    for i in MyBorder:
        charList.append(i)

    IsMyBorderEven = len(charList) % 2

    if IsMyBorderEven != 0:
        print("Needs to be re-worked into even characters!")
    else:
        finalize = list()
        for i in range(0, len(charList)/2, 1):
            finalize.append(''.join(charList[i]))
        finalize.append(MyString)
        for i in range((len(charList)/2), len(charList), 1):
            finalize.append(''.join(charList[i]))
        print(''.join(finalize))

makeoutword("<>","epic")
makeoutword("\\\\//", "superb")
makeoutword("vvvvv","This will not work.")
makeoutword("vvvv","This will work.")
makeoutword("------", " Goodbye. ")
'''
Output:

<epic>
\\superb//
Needs to be re-worked into even characters!
vvThis will work.vv
--- Goodbye. ---

'''
