'''
       ***************
       * LETTER SWAP *
       ***************

     Tommy H. Yeargin, Jr.
       April 30, 2017

'''
word = "everyman"
rack = list()
for i in word:
    rack.append(i)
newRack = list()
newRack.append(rack[-1])
for i in range(1, len(rack) - 1, 1):
    newRack.append(rack[i])
newRack.append(rack[0])
title = "* LETTER SWAP *"
print("{}\n{}\n{}".format((len(title)*"*"),title,(len(title)*"*")))
print("Old word: {}".format(word))
print("New word, with first and last letters exchanged: {}".format(''.join(newRack)))

'''
Output:

***************
* LETTER SWAP *
***************
Old word: everyman
New word, with first and last letters exchanged: nverymae

'''
