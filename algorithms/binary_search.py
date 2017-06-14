__author__ = 'bkapusta'
rlst = range(188)
# http://interactivepython.org/runestone/static/pythonds/SortSearch/TheBinarySearch.html
#----------------------------------------------------------------
# Binary searh while loop
# ---------------------------------------------------------------

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


#----------------------------------------------------------------
# Binary search recursive
# ---------------------------------------------------------------
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