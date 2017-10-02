'''
sort all the items in the list, except -1.
So, if you have list [5, 3, -1, 9, -1, 2, 0]
your function would return:
[0, 2, -1, 3, -1, 5, 9]
'''
import requests
from other.denis_class import Bob
babushka = Bob()
print(babushka.add_2_nums(4, 5))



# from interviewcake IMPORTANTO


print("==="*32)
l = [5, 3, -1, 9, -1, 2, 0]
# l = [1, 5, 2]
# l = []

def sort_except_minus_1(lst):
    if len(lst)==0:
        return lst
    if type(lst)!=list:
        raise Exception("Please enter list")
    print("Our list before", lst)
    positions_of_minus_1 = []
    for position, item in enumerate(lst):
        if item == -1:
            positions_of_minus_1.append(position)
    print("Indexes of -1 in original list:", positions_of_minus_1)
    lst.sort()
    # new_list = sorted(lst)
    # print("New list", new_list)
    print(lst)
    # number_of_minus_ones = len(positions_of_minus_1)
    # print("number of minus ones:", number_of_minus_ones)
    # list_with_no_minus_ones = lst[number_of_minus_ones:]
    # print("list with no minus ones:", list_with_no_minus_ones)
    # for minus_one_index in positions_of_minus_1:
    #     list_with_no_minus_ones.insert(minus_one_index, -1)
    # return list_with_no_minus_ones
print("Result:", sort_except_minus_1(l))
# sort_except_minus_1("Denis")
# print(sort_except_minus_1(l))
print("old list:", l)

# 1) You write a function;
#
#
#
#
#
#
# 2) How would you test it?