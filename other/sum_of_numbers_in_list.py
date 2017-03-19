"""
https://en.wikipedia.org/wiki/Knapsack_problem
http://stackoverflow.com/questions/3420937/algorithm-to-find-which-number-in-a-list-sum-up-to-a-certain-number
https://www.topcoder.com/community/data-science/data-science-tutorials/dynamic-programming-from-novice-to-advanced/
task
list = [1,2,3,10]
sum = 12
result = [2,10]
"""
lst1 = [1, 2, 3, 9]
lst2 = [1, 2, 4, 4]
lst = [1,2,3,10,2, 6, 3]
target = 8
import cProfile

def find_sum_from_the_list(sum, lst):
    result = []
    for index, elem in enumerate(lst):
        for j in lst[index:]:
            if elem+j==target and ([elem, j] not in result):
                result.append([elem, j])
                break

    return result

print find_sum_from_the_list(target, lst)

def sum_1(sum, lst):
    if len(lst)<2:
        raise ValueError("List must contain at least 2 values")
    smallest = lst[0]
    largest = lst[-1]
    print smallest, largest
    for index, elem in enumerate(lst):
        print "=== Current largest {0}\n === Current smallest {1}".format(largest, smallest)
        if smallest+largest == sum:
            return smallest, largest
        elif smallest+largest > sum:
            largest = lst[len(lst)-1-index]
            print "changed largest to: ", largest
        elif smallest+largest < sum:
            smallest = lst[index]
            print "changes smallest to: ", smallest
    return False

cProfile.run('''def sum_2(num, lst):
    diff = set()

    for item in lst:
        if item in diff:
            return [item, num-item], diff
        diff.add(num-item)
    return False
print sum_2(8, lst)''')

def sum_2(num, lst):
    diff = set()

    for item in lst:
        if item in diff:
            return [item, num-item], diff
        diff.add(num-item)
    return False
print sum_2(8, lst)

