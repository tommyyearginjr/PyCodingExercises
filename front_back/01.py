def front_back(word):
    rack = list()
    for i in word:
        rack.append(i)
    newRack = list()
    newRack.append(rack[-1])
    for i in range(1, len(rack) - 1, 1):
        newRack.append(rack[i])
    newRack.append(rack[0])
    print("Old word: {} --> New word w/ first and last letters exchanged: {}".format(word, ''.join(newRack)))

front_back('blossom')
front_back('openings')
