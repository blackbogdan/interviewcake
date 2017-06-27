__author__ = 'bkapusta'
'''
Your queue should have an enqueue and a dequeue function and it should be "first in first out" (FIFO).
'''
class queue_with_2_stacks:
    def __init__(self):
        # create 2 stacks
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, item):
        # append new items in the "in stack"
        return self.in_stack.append(item)

    def dequeue(self):
        # if length of "out_stack" is ==0 we pop items from
        # in_stack and append those to "out_stack".
        # With this approach we figure out the problem
        # of enqueue new items, and deque already existing
        # ones
        if len(self.out_stack)==0:

            while len(self.in_stack) > 0:
                self.out_stack.append(self.in_stack.pop())

            # in case there's nothing in the queue raise
            # Index Error
            if len(self.out_stack) == 0:
                raise IndexError("Can't dequeue from empty queue!")
        return self.out_stack.pop()
'''
complexity:
enqueue - O(1)
dequeu -  O(m)


'''

my_q = queue_with_2_stacks()
my_q.enqueue(1)
my_q.enqueue(2)
my_q.enqueue(3)
my_q.enqueue(4)
print my_q.in_stack
print my_q.dequeue()
print my_q.in_stack
print my_q.out_stack
my_q.enqueue(5)
my_q.enqueue("asdf")
print my_q.in_stack
print my_q.dequeue()
print my_q.dequeue()
print my_q.dequeue()
print my_q.dequeue()
print my_q.dequeue()