'''
Given an array of ints, and knowing that every int in it is nonunique except one, find the unique element.  Answer Question
'''

list_of_integers = [x for x in range(10)]+[y for y in range(11)] +[122]
print list_of_integers
print "set is", set(list_of_integers)
d = ['red', 'blue', 'red', 'green', 'blue', 'blue']


def count_words(dictionario):
    result = {}
    for element in dictionario:
        result[element]=result.get(element, 0) + 1
    keys = result.keys()
    values = result.values()
    z = keys[values.index(min(values))]
    return z

print count_words(d)
