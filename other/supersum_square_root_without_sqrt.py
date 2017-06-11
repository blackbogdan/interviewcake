'''find sum of numbers multiplied by it's index'''
x = [2, 3, 5, 2]
from math import sqrt
def super_sum(lst):
    my_sum = 0
    for index, item in enumerate(lst):
        my_sum +=index*item
    return my_sum



def square_root_through_binary_search(num):
    # took it from here: http://www.geeksforgeeks.org/square-root-of-an-integer/
    '''find square root whithout usin sqrt, abs'''
    if num in [0, 1]:
        return num
    elif num < 0:
        raise ValueError("Please enter positive number")
    start = 0
    end = num/2.0
    i = 0
    while start <= end:
        i += 1
        mid = (start + end)/2
        if mid*mid == num:
            return mid

        if mid*mid < num:
            start = mid + 1
            result = mid
        elif mid*mid > num:
            end = mid - 1
    return result

def square_root_with_loop(num):
    if num in [0, 1]:
        return num
    elif num < 0:
        raise ValueError("Please enter positive number")
    i = 0
    result = None
    while result<num:
        result = i*i
        if result == num:
            return i
        i+=1
    return i-1


if __name__== "__main__":
    # print super_sum(x)
    number = 999912399999998
    print "Result with binary tree: {}".format(square_root_through_binary_search(number))
    print "Result with loop: {}".format(square_root_with_loop(number))
    print "Python function result: {}".format(sqrt(number))