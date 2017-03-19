
from math import sqrt
from itertools import islice, count
for i in xrange(2, 10):
    print i
for i in islice(count(2),10):
    print "-----", i

def prime(num):
    for i in xrange(2, int(sqrt(num)+1)):
        print "verifying number", i
        print "reem", num % i
        if not num%i:

            return False
    return True

print prime(6)