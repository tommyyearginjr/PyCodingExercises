'''

Given a string, return a new string where "not " has been added to the front. However,
if the string already begins with "not", return the string unchanged.

'''

string = ""
def not_string(string):
    words = []
    words.append(string.split())
    if words[0][0] == 'not':
        print(string)
    else:
        print('not ' + string)

not_string("hello")
not_string("not too bad")
not_string("not so bad")
not_string("for pussies!")
