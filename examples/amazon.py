# Quality Assurance Development Engineer
# https://www.interviewzen.com/question/3XGpfYj

# 1st Interview QUESTION:
# Here are a few Open Ended Questions .
#
# Expected time for completion: 15 minutes
#
# •       Describe the activities in your current role and the percentage of time you spent on each?
#
# •       In your professional life what have you learned in the past six months? What would you like to learn in the next six months?
# I'm currently working as White Box QA Automation Engineer for Sony Interactive Entertainment (San Francisco). Started
# July 24-th
# I'm responsible for documenting test cases and automating those using Node JS. So, for the last 2 months I learnt
# Javascript and enchanced my knowledge in CSS locators.
# In my previous company I was also working as QA Automation Engineer. Using python, selenium and Robot Framework I
# automated various scenarios, for example:
# 1) UI Web (Including comparing UI output to SQL database content; Parsing Apache logs to retreive neceessary data for
# UI asserting);
# 2) REST Api;
# 3) Mobile Automation using Appium;
# Moreover, I helped to enhance our automation environment. Configured Jenkins environments, on various machines.

# In both companies I would say that 80% of my time is spent on Automation developement and 20% is Test Case Developement/
# Bug reporting/Stories Spec Review with PM and developers.


# What would you like to learn in the next six months?
# I would like to develop automation environment from scratch. Since the position is related to Amazon Prime, it
# would be really interesting to learn how the big data analysis is performed and which technologies are used during
# this process.


# TASK 2
2nd Interview Question :

2 -  Write a program that determines if a number is prime or not. Use any language. If your language includes a prime number calculation, you cannot use it. Feel free to lookup the definition of a prime number, but do not look up an example program. We expect you to be able to write this on your own.
```
A
prime
number( or a
prime) is
a
natural
number
greater
than
1
that
has
no
positive
divisors
other
than
1 and itself.
```
from math import sqrt
def isPrime(n):
    Cover cases of invalid input:
    if type(n) != int:
        raise Exception("Please enter integer number greater than 1")
    if n < 2:
        return False
    # If there're no positive devisors for number n from 2 to sqrt(n),
    # then there're no devisors of n
    # Needed to add + 1, since range generates up to but not including
    for i in range(2, int(sqrt(n)) + 1):  # assuming python 3 is used, then range will return generator.
        if not n % i:
            return False
    return True


def isPrimeOneLiner(n):
    # pythonic way to represent code above in one line:
    return n > 1 and all(n % i for i in range(2, int(sqrt(n)))



Task 3:


