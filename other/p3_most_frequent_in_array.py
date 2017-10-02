'''Find the maximum repeating number in O(n) time and O(1) extra space
Given an array of size n, the array contains numbers in range from 0 to k-1 where k is
a positive integer and k <= n. Find the maximum repeating number in this array.
For example, let k be 10 the given array be arr[] = {1, 2, 2, 2, 0, 2, 0, 2, 3, 8, 0, 9, 2, 3},
the maximum repeating number would be 2. Expected time complexity is O(n) and extra space allowed is O(1).
Modifications to array are allowed .'''


'''A better approach is to create a count array of size k and initialize all 
elements of count[] as 0. Iterate through all elements of input array, and for 
every element arr[i], increment count[arr[i]]. Finally, iterate through count[]
 and return the index with maximum value. This approach takes O(n) time, but requires O(k) space.

Following is the O(n) time and O(1) extra space approach. Let us understand the approach 
with a simple example where arr[] = {2, 3, 3, 5, 3, 4, 1, 7}, k = 8, n = 8 (number of elements in arr[]).

1) Iterate though input array arr[], for every element arr[i], increment arr[arr[i]%k] by k
 (arr[] becomes {2, 11, 11, 29, 11, 12, 1, 15 })

2) Find the maximum value in the modified array (maximum value is 29). 
Index of the maximum value is the maximum repeating element (index of 29 is 3).

3) If we want to get the original array back, we can iterate through the array 
one more time and do arr[i] = arr[i] % k where i varies from 0 to n-1.

How does the above algorithm work? Since we use arr[i]%k as index and add value k 
at the index arr[i]%k, the index which is equal to maximum repeating element will 
have the maximum value in the end. Note that k is added maximum number of times at
 the index equal to maximum repeating element and all array elements are smaller than k.'''

l = [2, 3, 4, 5, 3, 2, 2, 1]
# l = [1, 2, 3, 4, 5]
# sum is 15
# 1 +6
# 2+5
# 3+4
#
# 7*3 =21
# n = 5
# (n + 1)*(n/2)
#
# s= n-1
def most_frequent(lst):
    n = len(lst)
    print(lst)
    print("n is: ", n)
    for i in range(n):

        print("==>", i)
        print(lst[i], lst[i] % n)
        lst[lst[i]%n] += n
    print(lst)
    maximum = lst[0]
    result = 0
    for index, element in enumerate(lst):
        if index == 0:
            continue
        if element > maximum:
            maximum = element
            result = index
    return result

def m_f(lst):
    n = len(lst)
    print("n", n)
    maximum = 0
    index = 0
    for i in range(n):
        # print("==>", i)
        lst[lst[i] % n] += n
        element = lst[lst[i] % n]
        # print("max", maximum)
        # print("element",element)
        # print(lst)
        if element > maximum:
            maximum = element
            index = i
            # print("inside comparison. Maximum:", maximum, "Index:", index)
    # return index, lst[index] % n
    print("most Frequent", lst[index] % n)

    for index, number in enumerate(lst):
        # print(number)
        lst[index] = number % n
    print("====>",lst)
# print("Most Mostfrequent element in array:", most_frequent(l))
# print("Most frequent B:", m_f(l))
m_f(l)