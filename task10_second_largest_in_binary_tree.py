__author__ = 'bkapusta'
'''
Write a function to find the 2nd largest element in a binary search tree.
Here's a sample binary tree node class:
'''


class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def leftinsert(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def rightinsert(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

    def find


bst = BinaryTreeNode(15)
bst.leftinsert(10)
bst.rightinsert(20)
