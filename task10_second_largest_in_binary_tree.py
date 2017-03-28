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

    def find(self, data):
        # if data == value, then BOOOYA, we found the node
        if self.value == data:
            return True
        # in case data is present and it's value is less than current node
        elif self.value > data:
            if self.left:
                # call data recursively again to find data in the left node
                return self.left.find(data)
            else:
                return False
        # in case data is greater than current node, then go to the right of the tree
        elif self.value < data:
            if self.right:
                # call function recursively again to find data in the right subnode
                return self.right.find(data)
            else:
                return False

    def insert(self, data):
        # in case data already exists, return False
        if self.value == data:
            return False

        #  in case data is less than value of current node
        if self.value > data:
            if self.left:
                # if current node has left child, call function recursively
                return self.left.insert(data)
            else:
                # if no more left childen, create new node with data
                self.leftinsert(data)
                return True
        if self.value > data:
            if self.right:
                return self.right.insert(data)
            else:
                self.rightinsert(data)
                return True






l = [17, 2, 6, 16, 6, 20, 4, 16, 18, 16, 11]
# l = [2, 6, 16, 6, 20, 4, 16, 18, 16, 11]
# for item in l:
#     bst.insert(item)
# print bst.find(6)