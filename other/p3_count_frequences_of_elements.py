'''Count frequencies of all elements in array in O(1) extra space and O(n) time
Given an unsorted array of n integers which can contain integers from 1 to n.
Some elements can be repeated multiple times and some other elements can be absent from the array.
Count frequency of all elements that are present and print the missing elements.
http://www.geeksforgeeks.org/count-frequencies-elements-array-o1-extra-space-time/'''
'''https://stackoverflow.com/questions/1518522/python-most-common-element-in-a-list'''
a = [2, 3, 3, 2, 5, 1]


def find_frequences(lst):
    # nubmer of elements in list:
    n = len(lst)
    i = 0
    while i < n:
        print("=="*40)
        # if we already saw an element
        if lst[i] < 0:
            i += 1
            continue
        elementIndex = lst[i] - 1
        print(i, elementIndex)
        if lst[elementIndex] > 0:
            print(lst[elementIndex], "is greater than 0")
            lst[i] = lst[elementIndex]
            lst[elementIndex] = -1
            print(lst)
        else:
            print(lst[elementIndex], "is less than 0")
            lst[elementIndex] -= 1
            lst[i] = 0
            i += 1
    for j in range(n):
        print(j+1, "->", abs(lst[j]))

find_frequences(a)