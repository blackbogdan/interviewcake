# coding=utf-8
'''We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.

parrot_trouble(True, 6) → True
parrot_trouble(True, 7) → False
parrot_trouble(False, 6) → False'''

def parrot_trouble(talking, hour):
    return talking and (hour < 7 or hour > 20)
parrot_trouble(True, 6)

'''
Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.

makes10(9, 10) → True
makes10(9, 9) → False
makes10(1, 9) → True
'''
def makes10(a, b):
  return a==10 or b==10 or a+b==10

'''
Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.

near_hundred(93) → True
near_hundred(90) → True
near_hundred(89) → False'''
def near_hundred(n):
  return (abs(100 - n) <=10) or (abs(200 - n)<=10)


'''
Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.

pos_neg(1, -1, False) → True
pos_neg(-1, 1, False) → True
pos_neg(-4, -5, True) → True'''
def pos_neg(a, b, negative):
    return (a < 0 and b < 0) if negative else ((a < 0 and b > 0) or (a > 0 and b < 0))


'''
Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.

not_string('candy') → 'not candy'
not_string('x') → 'not x'
not_string('not bad') → 'not bad'"'''
def not_string(str):
  return str if str.startswith('not') else "not %s" % str


'''
Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).

missing_char('kitten', 1) → 'ktten'
missing_char('kitten', 0) → 'itten'
missing_char('kitten', 4) → 'kittn'"'''
def missing_char(str, n):
  return str[:n]+str[n+1:]


'''
Given a string, return a new string where the first and last chars have been exchanged.

front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'''''
def front_back(str):
  return  str if len(str)<=1 else str[-1]+str[1:-1]+str[0]


'''Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.
front3('Java') → 'JavJavJav'
front3('Chocolate') → 'ChoChoCho'
front3('abc') → 'abcabcabc'''''
def front3(str):
  return str*3 if len(str)<3 else str[:3]*3

'''
Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello'''''
def string_bits(str):
    result = ""
    for i in range(len(str)):
        if i %2 ==0:
            result = result+str[i]
    return result

def string_bits_2(str):
    return "".join([str[i] for i in range(len(str)) if i%2==0])

"""
Given a non-empty string like "Code" return a string like "CCoCodCode".

string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'"""
def string_splosion(str):
    result = ""
    for i in range(len(str)):
        result+=str[:i+1]
    # return result
    return "".join([str[:i+1] for i in range(len(str))])


"""
Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).

last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2"""

def last2(str):
    # Screen out too-short string case.
    if len(str) < 2:
        return 0

    # last 2 chars, can be written as str[-2:]
    last2 = str[-2:]
    count = 0

    # Check each substring length 2 starting at i
    for i in range(len(str) - 2):
        sub = str[i:i + 2]
        if sub == last2:
            count = count + 1

    # return count OR THIS
    # return len([1 for i in range(len(str) - 2) if str[i:i + 2] == str[-2:]])

"""Given an array of ints, return the number of 9's in the array.

array_count9([1, 2, 9]) → 1
array_count9([1, 9, 9]) → 2
array_count9([1, 9, 9, 3, 9]) → 3"""
def array_count9(nums):
  return len([1 for i in nums if i==9])

"""
Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.

array_front9([1, 2, 9, 3, 4]) → True
array_front9([1, 2, 3, 4, 9]) → False
array_front9([1, 2, 3, 4, 5]) → False"""
def array_front9(nums):
    # First figure the end for the loop
    end = len(nums)
    if end > 4:
        end = 4

    for i in range(end):  # loop over index [0, 1, 2, 3]
        if nums[i] == 9:
            return True
    return False


"""
Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.

array123([1, 1, 2, 3, 1]) → True
array123([1, 1, 2, 4, 1]) → False
array123([1, 1, 2, 1, 2, 3]) → True"""

def array123(nums):
  # Note: iterate with length-2, so can use i+1 and i+2 in the loop
  for i in range(len(nums)-2):
    if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
      return True
  return False

def array123_b(nums):
    return len(set(nums).intersection([1,2,3]))==3
    # return "123" in "".join(str(x) for x in nums)



"""
Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.

string_match('xxcaazz', 'xxbaaz') → 3
string_match('abc', 'abc') → 2
string_match('abc', 'axc') → 0"""


def string_match(a, b):
    # Figure which string is shorter.
    shorter = min(len(a), len(b))
    count = 0

    # Loop i over every substring starting spot.
    # Use length-1 here, so can use char str[i+1] in the loop
    for i in range(shorter - 1):
        a_sub = a[i:i + 2]
        b_sub = b[i:i + 2]
        if a_sub == b_sub:
            count = count + 1

    return count