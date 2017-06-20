
import sys

def merge_sort_interface(lst):

    global new_list
    new_list = [None]*len(lst)
    merge_sort(lst, 0, len(lst) - 1)
    return new_list


def merge_sort(lst, first_index, last_index):
    # if len(lst) > 1:
    if first_index < last_index:
        middle_index = (first_index + last_index) // 2
        merge_sort(lst, first_index, middle_index)
        merge_sort(lst, middle_index + 1, last_index)
        merge(lst, first_index, middle_index, last_index)

def merge(lst, first_index, middle_index, last_index):
    L = lst[first_index:middle_index]
    R = lst[middle_index:last_index+1]
    L.append(sys.maxint)
    R.append(sys.maxint)
    i = j = 0
    for k in range(first_index, last_index+1):
        if L[i] <= R[j]:
            # lst[k] = L[i]
            new_list[k] = L[i]
            i += 1
        else:
            # lst[k] = R[j]
            new_list[k] = R[j]
            j += 1

# print merge_sort_interface(random_list)



def merge_sort_while(lst):
    if len(lst)<2:
        return lst
    result = []
    mid = len(lst)//2
    l = merge_sort_while(lst[:mid])
    r = merge_sort_while(lst[mid:])
    while len(l)>0 and len(r)>0:
        if l[0]<r[0]:
            result.append(l.pop(0))
        else:
            result.append(r.pop(0))
    result +=l
    result +=r
    return result

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
    # while l and r lists are not empty
    while i < len(l) and j < len(r):
        print "left ", l
        print "right", r
        if l[i] < r[j]:
            print "Item in left list is less, appending it", l[i]
            result.append(l[i])
            i += 1
        else:
            print "Item in right list is less, appending it", r[i]
            result.append(r[j])
            j += 1
        print "current result list is:", result

    print l[i:]
    print r[j:]
    # Next 2 steps are needed when we have items left in one of the list
    # for example, left list was [2] and right list was [1,9] before the
    # while loop.
    # after while loop finished, we'll have result = [1, 2] and we'll
    # exit while loop since after appending 2 to the list i will become
    # 1 and expression while i < len(l) and j < len(r):
    # shall become 1<len(l) 1<1 ==> False.
    # But in the right list we'll have last item which is [9], and
    # we shall add it to the end of the list.
    # result += l[i:] ==> [1, 2] + l[1:] ==> [1, 2] + []
    # result += r[j:] ==> [1, 2] + r[1:] ==> [1, 2] + [9] = [1, 2, 9]
    result += l[i:]
    result += r[j:]
    print "result after result +=", result
    print "==========>"
    return result

if __name__=="__main__":
    random_list = [3, 5, 2, 1, 9]
    print random_list
    # print merge_sort_while(random_list)
    print msort3(random_list)
