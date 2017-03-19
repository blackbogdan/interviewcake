"""You have a list of integers, and for each index you want to find the product of every integer except the integer at that index.
Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products.

For example, given:

  [1, 7, 3, 4]

your function would return:

  [84, 12, 28, 21]

by calculating:

  [7*3*4, 1*3*4, 1*7*4, 1*7*3]

Do not use division in your solution."""

mr_list =   [2,3,0, 9]
mr_list2 = [-1, 7, 3, 4]
mr_list3 = [1, 0, 3, 4]
mr_list4 = [1, 0, 3, 5, 0]
#what if there'is empty list
#what if number of items are 1 or 2

def get_products_of_all_ints_except_at_index(int_list):
    if len(int_list)==1:
        return int_list
    # we make a list with the length of the input list to
    # hold our products
    products_of_all_ints_except_at_index = [None] * len(int_list)

    # for each integer, we find the product of all the integers
    # before it, storing the total product so far each time
    product_so_far = 1
    i = 0
    while i < len(int_list):
        products_of_all_ints_except_at_index[i] = product_so_far
        product_so_far *= int_list[i]
        i += 1

    # for each integer, we find the product of all the integers
    # after it. since each index in products already has the
    # product of all the integers before it, now we're storing
    # the total product of all other integers
    product_so_far = 1
    i = len(int_list) - 1
    while i >= 0:
        products_of_all_ints_except_at_index[i] *= product_so_far
        product_so_far *= int_list[i]
        i -= 1

    return products_of_all_ints_except_at_index

print get_products_of_all_ints_except_at_index(mr_list2)

def product_of_all(lst):
    mul = 1
    lst_of_zeros = []
    for item in lst:
        if item == 0:
            lst_of_zeros.append(item)
            if len(lst_of_zeros)>1:
                return [0]*len(lst)
        else:
            mul*=item

    if len(lst_of_zeros)==0:
        for index, num in enumerate(lst):
            lst[index] = mul/num
        return lst
    elif len(lst_of_zeros)==1:
        result = [0]*len(lst)
        result[lst.index(0)]=mul
        return result

# print product_of_all(mr_list2)