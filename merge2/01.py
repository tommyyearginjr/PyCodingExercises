'''
Start with two arrays of strings, A and B, each with its elements in alphabetical order and without duplicates. Return a new array containing the first N elements from the two arrays. The result array should be in alphabetical order and without duplicates. A and B will both have a length which is N or more. The best "linear" solution makes a single pass over A and B, taking advantage of the fact that they are in alphabetical order, copying elements directly to the new array.

mergeTwo(["a", "c", "z"], ["b", "f", "z"], 3) ---> ["a", "b", "c"]
mergeTwo(["a", "c", "z"], ["c", "f", "z"], 3) ---> ["a", "c", "f"]
mergeTwo(["f", "g", "z"], ["c", "f", "g"], 3) ---> ["c", "f", "g"]
'''
from collections import Counter

def mergeTwo(PuffDaddy01, PuffDaddy02, N):
    unique01counter = Counter(PuffDaddy01)
    unique01 = []
    for key in unique01counter:
        unique01.append(key)
    unique01 = sorted(unique01)
    unique02counter = Counter(PuffDaddy02)
    unique02 = []
    for key in unique02counter:
        unique02.append(key)
    unique02 = sorted(unique02)
    ParisJackson = []
    BlanketJackson = []
    for i in range(0, N-1, 1):
        ParisJackson.append(unique01[i])
    for i in range(0, N-1, 1):
        if unique02[i] in ParisJackson:
            pass
        else:
            ParisJackson.append(unique02[i])
    ParisJackson = sorted(ParisJackson)
    for i in range(0, N, 1):
        BlanketJackson.append(ParisJackson[i])
    print('{}, {}, {} {} {}'.format(unique01, unique02, N, ' --> ', BlanketJackson))

mergeTwo(["a", "c", "z"], ["b", "f", "z"], 3)
mergeTwo(["a", "c", "z"], ["c", "f", "z"], 3)
mergeTwo(["f", "g", "z"], ["c", "f", "g"], 3)
print(72*'-')
mergeTwo(['j','a','y','y','o','u','n','g','b','l','o','o','d'],['z','e','e','m','a','x'],5)
