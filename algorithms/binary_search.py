__author__ = 'bkapusta'
rlst = range(100000000)
# http://interactivepython.org/runestone/static/pythonds/SortSearch/TheBinarySearch.html
def binary_search(lst, item):
    first = 0
    last = len(lst) - 1

    while first<=last:
        mid = (first+last)//2
        if lst[mid] == item:
            return mid
        elif item<lst[mid]:
            last = mid - 1
        else:
            first = mid +1
    return False
def binary_recursive(lst, item):
    if len(lst)==0:
        return False
    else:
        mid = len(lst)//2
        if lst[mid]==item:
            return False
        elif item < lst[mid]:
            return binary_recursive(lst[:mid], item)
        else:
            return binary_recursive(lst[mid+1:], item)
binary_search(rlst, -1)
binary_recursive(rlst, -1)
# print rlst.index(14)