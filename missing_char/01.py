'''
        *************************
        * REMOVE THIS CHARACTER *
        *************************

          Tommy H. Yeargin, Jr.
             April 30, 2017

'''
JoeCronin = "Joe Cronin"
removeThisCharacter = len(JoeCronin) - 3
rack = list()
for i in JoeCronin:
    rack.append(i)
newRack = list()
for i in range(0, len(JoeCronin), 1):
    if i != removeThisCharacter:
        newRack.append(rack[i])
title = "* REMOVE THIS CHARACTER *"
print("{}\n{}\n{}".format((len(title)*"*"),title,(len(title)*"*")))
print("Old string: {}".format(JoeCronin))
print("Character to remove: #{} ---> {}".format(removeThisCharacter+1,rack[removeThisCharacter]))
print("New string: {}".format(''.join(newRack)))
'''

Output:

*************************
* REMOVE THIS CHARACTER *
*************************
Old string: Joe Cronin
Character to remove: #8 ---> n
New string: Joe Croin

'''
