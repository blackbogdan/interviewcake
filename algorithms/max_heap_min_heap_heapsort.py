# Joe James Max Heap: https://www.youtube.com/watch?v=GnKHVXv_rlQ
class MaxHeap:
    def __init__(self, lst=[]):
        self.heap = [0]
        for i in lst:
            # append item in the end of the heap
            self.heap.append(i)
            # position correctly new appended item in the heap
            self.__floatUp(len(self.heap) - 1)

    def push(self, data):
        self.heap.append(data)
        self.__floatUp(len(self.heap) - 1)

    def peek(self):
        # if item exists in the heap, return it
        if self.heap[1]:
            return self.heap[1]
        else:
            # no items in the heap:
            return False

    def pop(self):
        #  there're 2 or more values in the heap.
        #  we need to swap first(root) value with the last one. Delete last item and then
        #  bubble down (heapify) new value located in heap[1] first position
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) -1)
            # this will remove last value from the list and return it
            max = self.heap.pop()
            self.__bubbleDown(1)
        # there's only one value in the heap, simply we pop it
        elif len(self.heap) == 2:
            max = self.heap.pop()

        # there're no values in the heap, return False
        else:
            max = False
        return max

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatUp(self, index):

        parent_index = index//2

        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent_index]:
            self.__swap(index, parent_index)
            self.__floatUp(parent_index)

    def __bubbleDown(self, index):
        # in some casese it's called "heapify"
        # left_child_index
        left = index * 2
        # right_child_index
        right = index * 2 + 1
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.__swap(index, largest)
            return self.__bubbleDown(largest)
    def heap_sort(self):
        self.sorted_list = []
        popped_item = self.pop()
        while popped_item != False:
            self.sorted_list.append(popped_item)
            popped_item = self.pop()
        return self.sorted_list
# the_list = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
# m = MaxHeap([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
# from random import randint
# m.push(10)
# [m.push(randint(0, 18888)) for i in range(10) ]
# sorted_list = [m.pop() for i in xrange(len(m.heap)-1)]
# print m.heap
# print m.heap_sort()


#------------------------------------------------------
# ------------------------heap_sort other implementation:
#------------------------------------------------------
# https://stackoverflow.com/questions/13979714/heap-sort-how-to-sort
class other_max_heap_sort:
    def __init__(self, input_list):
        self.lst = input_list

    def swap(self, i, j):
        self.lst[i], self.lst[j] = self.lst[j], self.lst[i]

    def heapify(self, end, index):
        # these are the indexes of the chilren of current index:
        l_child = 2 * index
        r_child = 2 * index + 1
        largest = index
        if l_child < end and self.lst[largest] < self.lst[l_child]:
            largest = l_child
        if r_child < end and self.lst[largest] < self.lst[r_child]:
            largest = r_child
        if largest != index:
            self.swap(index, largest)
            self.heapify(end, largest)

    def heap_sort(self):
        end = len(self.lst)
        start = end//2 - 1
        for i in xrange(end, -1, -1):
            # print "calling heapify from heap sort", i
            self.heapify(end, i)

        for i in range(end-1, 0, -1):
            self.swap(i, 0)
            self.heapify(i, 0)
        return self.lst


class MinHeap:
    def __init__(self, input_data=[]):
        # occupying index 0
        self.heap = [0]
        for i in input_data:
            self.heap.append(i)
            self.__floatUP(len(self.heap) -1 )


    def __floatUP(self, index):
        # parent index p_i
        p_i = index//2
        if index <= 1:
            return
        elif self.heap[index] < self.heap[p_i]:
            self.__swap(index, p_i)
            self.__floatUP(p_i)

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def pop(self):
        if len(self.heap) > 2:
            # we swap value from the top to the latest one
            self.__swap(1, len(self.heap) - 1)
            # pop the value from the list
            min = self.heap.pop()
            self.__bubbleDOWN(1)
        elif len(self.heap) == 2:
            min = self.heap.pop()
        else:
            # no value in the heap
            min = False
        return min

    def __bubbleDOWN(self, index):
        l_child = 2*index
        r_child = 2*index + 1
        smallest_index = index
        # if we're having the left child "len(self.heap) > l_child". If this statement is False,
        # then we're overshooting the current heap and hence, we don't need to do anything
        if len(self.heap) > l_child and self.heap[smallest_index] > self.heap[l_child]:
            # in case item at smallest_index (which is current "index") we reassign the smallest index
            # to left child index
            smallest_index = l_child

        if len(self.heap) > r_child and self.heap[smallest_index] > self.heap[r_child]:
            smallest_index = r_child
#         at this point we determined item at which index is the smallest and the index of theat item

        # in case the index of smallest item is not equal to current index (meaning we current item positioned
        # incorrectly and we have children of current node)
        if smallest_index != index:
            # we swap item on the current postion with the smallest one. And call __bubleDOWN again on
            # the item of our swapped position at smallest_index
            self.__swap(index, smallest_index)
            return self.__bubbleDOWN(smallest_index)

    def push(self, value):
        self.heap.append(value)
        self.__floatUP(len(self.heap)-1)


if __name__ == "__main__":
    sqc = [2, 7, 1, -2, 56, 5, 3]
    min_heap = MinHeap(sqc)
    min_heap.push(10)
    min_heap.push(11)
    min_heap.push(-3)
    print min_heap.heap
    for i in range(len(sqc)-1):
        print min_heap.pop()
    # h = other_max_heap_sort(sqc)
    # print h.heap_sort()
    # print sqc, "YO mmama"
