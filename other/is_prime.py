from math import sqrt
from itertools import count, islice

# def isPrime(n):
#     return n> 1 and all(n % i for i in islice(count(2), int(sqrt(n) - 1)))


def isPrime(n):
    # if type(n)!='int':
    #     raise ValueError('This number is not a prime number, c\'mon')
    if n < 2:
        return False
    print sqrt(n)
    for i in islice(count(2), int(sqrt(n)-1)):
        print i
        print "reminder", n%i
        if not n%i:
            return False
    return True
print isPrime(13)


def is_it_prime(n):
    # if n < 2:
    #     return False
    # for i in islice(count(2), int(sqrt(n)-1)):
    #     if not n%i:
    #         return False
    # return True

    return n>1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))
print is_it_prime(13)
