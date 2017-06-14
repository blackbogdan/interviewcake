__author__ = 'bkapusta'
numba = 89
# how to count big fibonacci numbers:
# https://stackoverflow.com/questions/28548457/nth-fibonacci-number-for-n-as-big-as-1019
# why modulo?
def count_fibo_bottom_up(num=numba):
    if num < 0:
        raise ValueError("Fibonacci number must be greater than 0")
    elif num in [0, 1]:
        return num


    prev_prev = 0
    prev_num = 1

    for counter in xrange(num-1):
        # prev_num, current_number = current_number, current_number+number
        current_number = prev_prev + prev_num
        prev_prev = prev_num
        prev_num = current_number

    return current_number


def fib_recursive(num=numba):
    if num in [0,1]:
        return num
    return fib_recursive(num - 1) + fib_recursive(num - 2)


class memo_fib:
    def __init__(self):
        self.memo = {}

    def fib_recursive_memo(self, num):
        if num in [0, 1]:
            return num
        elif num in self.memo:
            return self.memo[num]

        result = fib_recursive(num-1) + fib_recursive(num - 2)
        self.memo[num] = result
        return result
#----------------------------------------------------------------
# Fibonacci with power
# ---------------------------------------------------------------
# with the matrix multiplication:
    # https://stackoverflow.com/questions/28548457/nth-fibonacci-number-for-n-as-big-as-1019
fib_matrix=[[1, 1],
            [1, 0]]
def matrix_mul(A, B, mod):
    if mod is not None:
        return [[(A[0][0]*B[0][0] + A[0][1]*B[1][0])%mod, (A[0][0]*B[0][1] + A[0][1]*B[1][1])%mod],
                [(A[1][0]*B[0][0] + A[1][1]*B[1][0])%mod, (A[1][0]*B[0][1] + A[1][1]*B[1][1])%mod]]
def matrix_square(A, mod):
    return matrix_mul(A,A,mod)

def matrix_pow(M, power, mod):

    # how to count big fibonacci numbers:
    # https://stackoverflow.com/questions/28548457/nth-fibonacci-number-for-n-as-big-as-1019
    # why modulo?
    # https://codeaccepted.wordpress.com/2014/02/15/output-the-answer-modulo-109-7/
    #Special definition for power=0:
    if power <= 0:
      return M
    print bin(power)
    # we need to reverse, since we need to begin with lowest number, which would be 0**1
    powers = list(reversed([True if i=="1" else False for i in bin(power)[2:]])) #Order is 1,2,4,8,16,...
    print powers
    print len(powers)
    matrices = [None for _ in powers]
    print matrices
    matrices[0] = M

    for i in range(1,len(powers)):
        matrices[i] = matrix_square(matrices[i-1], mod)
    print matrices

    result = None

    # here we need to matrixes that correspond to particular power. So, in order to get 100-th fibonacci number,
    # we would need to multiply matrix that correspond to 64-th, 32-nd and 4-th parameter.
    for matrix, power in zip(matrices, powers):
        print "===>Matrix {}. Power: {}".format(matrix, power)
        if power:
            if result is None:
                result = matrix
            else:
                result = matrix_mul(result, matrix, mod)

    return result
# print matrix_pow(fib_matrix, 6, 1000000007)[0][1]
# output:
# 0b110
# [False, True, True]
# 3
# [None, None, None]
# [[[1, 1], [1, 0]], [[2, 1], [1, 1]], [[5, 3], [3, 2]]]
# ===>Matrix [[1, 1], [1, 0]]. Power: False
# ===>Matrix [[2, 1], [1, 1]]. Power: True
# ===>Matrix [[5, 3], [3, 2]]. Power: True
# 8

# end of with matrix multiplication



if __name__=="__main__":
    print count_fibo_bottom_up()
    # fib_class = memo_fib()
    # fib_class.fib_recursive_memo(numba)
    # fib_recursive()
    # print fib_recursive_power(numba)
    print matrix_pow(fib_matrix, 6, 1000000007)[0][1]
    # print matrix_pow(fib_matrix, 10**2, 2)