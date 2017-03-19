lst = [2,3,4,56,7]
from itertools import islice
def highest_product_of_3(lst):
    if len(lst)<3:
        raise Exception("Less than 3 items!!!")
    highest_num = max(lst[0], lst[1])
    lowest_num = min(lst[0], lst[1])
    highest_product_of_two = lst[0]*lst[1]
    lowest_product_of_two = lst[0]*lst[1]

    highest_product_of_three = lst[0]*lst[1]*lst[3]
    for current in islice(lst, 2):
        highest_product_of_three = max(highest_product_of_three,
                                       current*highest_product_of_two,
                                       current*lowest_product_of_two)

        highest_product_of_two = max(highest_product_of_two,
                                     current*highest_num,
                                     current*lowest_num)
        lowest_product_of_two = min(lowest_product_of_two,
                                    current*highest_num,
                                    current*lowest_num)
        highest_num = max(highest_num, current)
        lowest_num = min(highest_num, current)

    return highest_product_of_three