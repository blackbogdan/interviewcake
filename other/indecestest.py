__author__ = 'bkapusta'
# glassdoor TESLA: https://www.glassdoor.com/Interview/Given-a-phone-number-write-an-algorithm-to-print-all-possible-alpha-codes-that-correspond-to-it-QTN_171562.htm
#
B = [1, 2, 3]


A = [-1, 3, -4, 5, 1, -6, 2, 1]
def solution(A):
    a = 0
    b = sum(A)
    # print "sum: ", b
    # for i, item in enumerate(A):
    #     print "iteration nubmer: ", i
    #     b-= A[i]
    #     print "current a:", a
    #     print "current b:", b
    #     if a==b:
    #         return i
    #     a += A[i]
    #
    # return -1
    for i in xrange(len(A)):
        b-=A[i]
        if a==b:
            return i
        a +=A[i]
    return -1


print solution(A)