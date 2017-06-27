__author__ = 'bkapusta'
'''
how to reverse a list:
'''
# first way
def reverse1():
    l = [3, 5, 8, 13]
    l.reverse()
    return l

def reverse_with_sort():
    l = [3, 5, 8, 13]
    l.sort(reverse=True)
    return l

def sort_with_function():
    l = [3, 5, 8, 13]
    new_list = sorted(l, reverse=True)


'''
How to compute n-th Fibonacci
number
'''
def fibonacci(num):
    '''The Fibonacci series is a numerical series
    where each item is the sum of the two previous items.
    It starts off like this:
    0,1,1,2,3,5,8,13,21...'''
    if num < 0:
        raise ValueError("Fibonacci number must be greater than 0")
    elif num in [0, 1]:
        return num

    prev_prev = 0
    prev_num = 1

    for counter in xrange(num-1):
        current_number = prev_prev + prev_num
        prev_prev = prev_num
        prev_num = current_number

    return current_number
# print fibonacci(6)
#prints 8



'''
Count words in file. Content of the file "unsorted.txt":
squirrel in mirror, justin timberlake. Mirror
squirrel loves mirrors, mirrors
yoyoyo, YoYOyO
MIrrors
'''
def count_words_in_file(filepath):

    result_dictionary = {}
    # this construction will open the file
    # and in case something fails,
    # it will close the file
    with open(filepath, 'r') as f:
        for line in f:
            # at the end of each line there's a
            # new line character "\n", let's
            # remove it.
            # line will
            line = line.strip()

            # line.split() will return list of words
            for word in line.split():
                # we need to lowercase all words, so
                # "Mirror" and "mirror" shall be counted
                # as one word
                word = word.lower()
                # in the text there could be commas and
                # dots, this shall remove those
                if word.endswith((".", ",")):
                    word = word[:-1]

                result_dictionary[word] = result_dictionary.get(word, 0) + 1
    return result_dictionary
print count_words_in_file('/Users/bkapusta/Downloads/Chrome/interviewcake/other/unsorted.txt')
#     prints out
#     {'justin': 1, 'mirrors': 3, 'timberlake': 1, 'in': 1, 'yoyoyo': 2, 'loves': 1, 'mirror': 2, 'squirrel': 2}


'''
Find most frequently used word in the file
'''
def most_frequently_used_word_in_file(filepath):
    # call the function "count_words_in_file"
    dict_with_words = count_words_in_file(filepath)
    # now "dict_with_words" variable contains:
    # {'justin': 1, 'mirrors': 3, 'timberlake': 1, 'in': 1, 'yoyoyo': 2, 'loves': 1, 'mirror': 2, 'squirrel': 2}

    # get only values form the dictionary
    values = dict_with_words.values()

    # get only keys from the dictionary
    keys = dict_with_words.keys()

    # get maximum value (this value is maximum number the key was met
    max_value = max(values)
    max_value_index = values.index(max_value)
    max_value_word = keys[max_value_index]
    return "Most frequently used word is: \"{}\". Number of times it was used: {}.".format(max_value_word, max_value)
print most_frequently_used_word_in_file('/Users/bkapusta/Downloads/Chrome/interviewcake/other/unsorted.txt')


'''
we have the list with 1 missing number.
Numbers in the list are increasing by 1. From 1 to 1000000
What is this number?
'''
l = [2, 1, 3, 5, 7, 6] #made missing number 4
# l = [1, 2, 3, 4, 5]
def find_missing_number(lst):
    # is the list sorted? If it's not, we need to sort it:
    lst.sort()
    lst_len = len(lst)
    for index, number in enumerate(lst):
        # if next number minus current number
        # is equal to 2, then we found the number
        # For example: 5-3 ==2. Then missing number
        # is 3+1 = 4
        # Another example is: 2-1==2 ==>False,
        # we don't have missing nubmer
        if lst[index+1] - lst[index] == 2:
            return number+1
        if index + 1 == lst_len - 1:
            # in case we have index + 1 equal to last index
            # of the list, we checked all numbers in list
            return False #we did not find the missing nubmer

print find_missing_number(l)


"""
let's say we have a list of numbers and some number.
For example: [3, 4, 19, 1, 5, -1], number =8

Is there 2 numbers in the list that in sum can return 8?
"""
def find_sum(lst, sum_to_match):
    # Solution idea:
    # Loop through the list.
    # With each iteration find subtraction between desired sum
    # and current number add that subtraction to set.
    # If that number is present in subtraction_set,
    # then we found 2 numbers that match desired sum
    subtraction_set = set()
    for number in lst:
        if number in subtraction_set:
            return number, sum_to_match - number
        subtraction_set.add(sum_to_match - number)
    return False #there's no numbers to match the sum

print find_sum([3, 4, 19, 1, 5, -1], 8)
# prints out (5, 3)
print find_sum([3, 4, 19, 1, 5, -1], 300)
# prints False