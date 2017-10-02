# coding=utf-8
# https://github.com/joeyajames/Python/blob/master/SortingAlgorithms.py
import sys
'''Bubble sort
Let’s say we have list [3, 2, 4, 1].
Loop through the list comparing 2 numbers.
Is 3 less than 2 ---> no, swap 3 with 2. We get: [2, 3, 4, 1]
Is 3 less than 4 ---> yes. Continue
Is 4 less than 1 ---> no. Swap 4 and 1. We get [2,3,1,4]
---
Is 2 less than 3 --->yes. Continue
Is 3 less than 1 --->no. Swap 3 and 1. We get [2, 1, 3, 4]
We don’t need to compare 3 and 4 now, because we know that 4 is a maximum number on the list. We go back to 2 and 1.
Is 2 less than 1 ---> no. Swap 2 and 1. We get [1, 2, 3, 4]

'''
from random import randint
MyLst = [3, 2, 4, 1]
# random_list= [randint(1, 10) for i in xrange(20)]
#---------------------------------------
# Bubble Sort
#---------------------------------------
def BubbleSort(lst):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

#---------------------------------------
# Quick Sort
#---------------------------------------
# https://www.youtube.com/watch?v=CB_NCoxzQnk
'''
1) We get the pivot (a value against we compare)
2) Call recursively function quck_sort2 until length of the list is ==1 (low_index < high_index:)
3) Quick_sort2 call partition function to:
    3.1) get pivot by selecting median value;
    3.2) swap pivot index item in the list with current lower_index item
    3.3) Define border(wall) as a lower index
    3.4) Make sorting of the list, updating border each time we have lst[i] < pivot_value
    3.5) Swap pivot value to the lower_index item value
    3.6) returns border index
4) Call recursively quick sort again 2 times:
    4.1) on left partition: quick_sort2(lst, low_index, border_from_3.6 - 1)
    4.2) on right partition: quick_sort2(lst, border_from_3.6 + 1, high_index)
'''

def quick_sort_interface(lst):
    quick_sort2(lst, 0, len(lst)-1)
    return lst
def quick_sort2(lst, low_index, high_index):
    # if there's more than one item to be sorted
    if low_index < high_index:
        p = partition(lst, low_index, high_index)
        quick_sort2(lst, low_index, p - 1)
        quick_sort2(lst, p + 1, high_index)

def get_pivot(lst, low_index, high_index):
    mid = (high_index + low_index) //2
    s = sorted([lst[low_index], lst[mid], lst[high_index]])
    # we need to return index of item from s:
    if s[1] == lst[low_index]:
        return low_index
    elif s[1] == lst[mid]:
        return mid
    return high_index

def partition(lst, low_index, high_index):
    pivot_index = get_pivot(lst, low_index, high_index)
    pivot_value = lst[pivot_index]
    lst[pivot_index], lst[low_index] = lst[low_index], lst[pivot_index]
    border = low_index
    # print border
    for i in range(low_index, high_index+1):
        # comparing pivot to current value in the list,
        if lst[i] < pivot_value:
            border+=1
            lst[i], lst[border] = lst[border], lst[i]
    # here we're swaping border with low index
    lst[low_index], lst[border] = lst[border], lst[low_index]
    return border


#---------------------------------------
# Merge Sort
#---------------------------------------
def merge_sort(lst):
    merge_sort2(lst, 0, len(lst)-1)
    return lst
def merge_sort2(lst, first_index, last_index):
    if  first_index < last_index:
        middle_index = (first_index + last_index)//2
        merge_sort2(lst, first_index, middle_index)
        merge_sort2(lst, middle_index+1, last_index)
        merge(lst, first_index, middle_index, last_index)

def merge(lst, first_index, middle_index, last_index):
    L = lst[first_index:middle_index]
    R = lst[middle_index:last_index+1]
    # in case list shall be odd, we will have "IndexError: list index out of range"
    # Workaround is to append maximum value possible for the list
    L.append(999999999)
    R.append(999999999)
    i = j = 0
    # print lst
    for k in range(first_index, last_index+1):
        if L[i] <= R[j]:
            lst[k] = L[i]
            i += 1
        else:
            lst[k] = R[j]
            j += 1

def msort3(x):
    result = []
    if len(x) < 2:
        return x
    # mid = int(len(x) / 2)
    mid = len(x)//2
    l = msort3(x[:mid])
    r = msort3(x[mid:])
    i = 0
    j = 0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1
        print result

    result += l[i:]
    result += r[j:]
    return result



if __name__=='__main__':
    random_list = [7, 10, 1, 9, 8, 9, 5, 4, 7, 3, 8, 4, 4, 7, 1, 5, 1, 4, 5]
    random_list = [3, 5, 2, 1, 9]
    # random_list= [randint(1, 100000) for i in xrange(1000)]
    # print sys.maxint
    # print len(random_list)
    sorted_list = [1, 1, 1, 3, 4, 4, 4, 4, 5, 5, 5, 5, 7, 7, 7, 8, 8, 9, 9, 10]
    # print BubbleSort(MyLst)
    # print random_list
    # print BubbleSort(random_list)
    # print quick_sort_interface(random_list)
    print  merge_sort(random_list)



