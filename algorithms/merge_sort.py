random_list = [3, 5, 2, 1, 9]
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
    while i < len(l) and j < len(r):
        print "left ", l
        print "right", r
        if l[i] < r[j]:
            print "less, appeindin", l[i]
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1
        print result

    result += l[i:]
    result += r[j:]
    return result

if __name__=="__main__":
    print random_list
    # print merge_sort_while(random_list)
    print msort3(random_list)
