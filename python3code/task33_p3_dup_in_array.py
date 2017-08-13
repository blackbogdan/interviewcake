# I have a list of n+1 numbers. Every number in range 1...n appears once except one number
# which appears twice
# Write a function to find that number
# https://www.interviewcake.com/question/python/which-appears-twice
# assuming that we have orded list, then this is the triangle model
# Which has features:
# first + last = second first +second last = len(l) + 1
# but we have a duplicate, then it will be len(l)
# assuming the list is ordered, because numbers in the range 1...n we can continue:

# we can figure it out in O(n)
def find_dup_bogdan(lst):
    if len(l)<2:
        raise Exception("Number of items in the list is less than 2")
    prev_num = lst[0]
    for index, current_num in enumerate(lst):
        if index == 0:
            continue
        if prev_num - current_num == 0:
            return current_num
        else:
            prev_num = current_num
    return "No duplicates in the list"


# another approach
def find_dup_with_sum(lst, n):
    # this handels if the list is unsorted
    # find the sum of numbers of equivalent list, using formula of triangle series:
    sum_of_numbers_within_range = (n**2 + n)//2
    print("Sum of nubmers within range: ", sum_of_numbers_within_range)
    # find sum of the current list
    sum_of_nubmers_in_lst = sum(lst)
    print("Sum of numbers in the given list: ", sum_of_nubmers_in_lst)
    # the difference between those would be the duplicated number
    return "duplicate number is: {}".format(sum_of_nubmers_in_lst - sum_of_numbers_within_range)

def find_repeat(numbers):
    numbers_seen = set()
    for number in numbers:
        if number in numbers_seen:
            return number
        else:
            numbers_seen.add(number)
    # whoops--no duplicate
    raise Exception('no duplicate!')

if __name__ == "__main__":
    l = [1, 2, 3, 4, 5, 5, 6, 7, 8]
    # l = []
    # print(find_dup_bogdan(l))
    print(find_dup_with_sum(l, 8))