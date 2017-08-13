# Find a duplicate, Space Edition™.
# We have a list of integers, where:
#
# The integers are in the range 1..n1..n
# The list has a length of n+1n+1
# It follows that our list has at least one integer which appears at least twice.
# But it may have several duplicates, and each duplicate may appear more than twice.
#
# Write a function which finds an integer that appears more than once in our list.
# (If there are multiple duplicates, you only need to find one of them.)

# We're going to run this function on our new, super-hip Macbook Pro With Retina Display™.
#  Thing is, the damn thing came with the RAM soldered right to the motherboard, so we can't
# upgrade our RAM. So we need to optimize for space!

# solution: use binary search approach.
# We look if the nubmer in current lower range. If it's not than it's in the second lowerr range.
# "range" is defined taking in consideratin the fact, that non duplicate values are 1...n.
# And duplicate is "+1". So, in some case we'll have "extra" value in our range. Narrowing down
# the range with "While" loop we'll get eventually to the number that is our duplicate.
# However, if there're no duplicates, it would return the last eelement in the list

# We binary search possiblity of current item appearing in the list. IF the item is not
# in current range, then it must be in second half range
# 1) Find the number of integers in our input list which lie within the range 1...n/2
# 2) Compare that to the number of possible unique integers in the same range.
# 3) If the number of actual integers is greater than the number of possible integers, we know
# there’s a duplicate in the range 1...n/2​​, so we iteratively use the same approach on that range.
# 4)If the number of actual integers is not greater than the number of possible integers,
# we know there must be duplicate in the range n/2...1..n,
# so we iteratively use the same approach on that range.
# 5)_At some point our range will contain just 1 integer, which will be our answer.

from random import shuffle
def find_repeat(the_list):
    #   floor is one, because according to task, we have range of numbers 1...n +1
    floor = 1
    # ceiling is this, because, non-duplicate amount would be 1...n, which is "len(lst) - 1
    # because total number of elements is 1...n+1 (+1 is for duplicated number)
    ceiling = len(the_list) - 1

    while floor < ceiling:
        print("===="*30)
        print("current floor: {}. current ceiling: {}".format(floor, ceiling))
        # divide our range 1..n into an upper range and lower range
        # (such that they don't overlap)
        # lower range is floor..midpoint
        # upper range is midpoint+1..ceiling
        midpoint = floor + ((ceiling - floor) // 2)
        lower_range_floor, lower_range_ceiling = floor, midpoint
        upper_range_floor, upper_range_ceiling = midpoint + 1, ceiling
        print("Lower_range_floor: {}, Lower_range_ceiling: {}\nUpper_range_floor: {}, "
              "Upper_range_ceiling: {}".\
              format(lower_range_floor, lower_range_ceiling,\
                     upper_range_floor, upper_range_ceiling))
        print("Current numbers: {}, {}, {}, {}".format(the_list[lower_range_floor], the_list[lower_range_ceiling],\
                                                   the_list[upper_range_floor], the_list[upper_range_ceiling]))
        # count number of items in lower range
        items_in_lower_range = 0
        for item in the_list:
            # is it in the lower range?
            if item >= lower_range_floor and item <= lower_range_ceiling:
                items_in_lower_range += 1

        distinct_possible_integers_in_lower_range = \
            lower_range_ceiling - lower_range_floor + 1


        if items_in_lower_range > distinct_possible_integers_in_lower_range:
            # there must be a duplicate in the lower range
            # so use the same approach iteratively on that range
            floor, ceiling = lower_range_floor, lower_range_ceiling
        else:
            # there must be a duplicate in the upper range
            # so use the same approach iteratively on that range
            floor, ceiling = upper_range_floor, upper_range_ceiling

    # floor and ceiling have converged
    # we found a number that repeats!
    return floor

if __name__ == "__main__":
    l = [1, 2, 3, 4, 10, 10, 6, 7, 8]
    l = [1, 4, 6, 8, 7, 5, 3, 2, 6]
    # print(shuffle(l))
    print(l)
    #
    # l = [1, 2, 3, 4, 5, 6, 7, 8]
    z=find_repeat(l)
    print(z,l[z])