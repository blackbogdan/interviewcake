__author__ = 'bkapusta'
# Binary tree explained:
# https://www.youtube.com/watch?v=YlgPi75hIBc&index=7&list=PLj8W7XIvO93qsmdxbaDpIvM1KCyNO1K_c
#
# traversal explained:
# http://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/

class Node:
    def __init__(self, val):
        self.value = val
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        '''
        so, this function diggs recursively to find out where to put new element.
        If it puts it successfully, it returns True
        It shall only return False in case data already exists in the tree
        '''
        if self.value == data:
            # in case node already exist, we won't add it. (Do not allow duplicates in the list)
            return False
        # if data that we're trying to insert is less than current node:
        elif self.value > data:
            if self.leftChild:
                # if there's a left child, call function again recursively
                return self.leftChild.insert(data)
            else:
                # if there's no left child, insert one and return True
                self.leftChild = Node(data)
                return True
        # if data that we're trying to insert is greater than current node:
        elif self.value < data:
            # if there's a right child, call function recursively
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                # if there's no more right childred, create one
                self.rightChild = Node(data)
                return True
    def find(self, data):
        # if data we're looking for is current value, then
        # Boooya, we found data
        if (self.value == data):
            return True

        elif self.value > data:
            # in case data is present and it's value is less than current node:
            if self.leftChild:
                # call recursively finction again to find data in the next left node
                return self.leftChild.find(data)
            else:
                return False
        elif self.value < data:
            # in case data is present and it's value is greater than current node:
            if self.rightChild:
                # call recursively function again to find data in the next right node
                return self.rightChild.find(data)
            else:
                return False
class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            # if root node doesn't exist, create one:
            return self.root.insert(data)
        else:
            # if root node exists, create new node
            self.root = Node(data)
            # return "True" if node was added
            return True

    def find(self, data):
        if self.root:
            # if root exists, call "find" function on the root node
            return self.root.find(data)
        else:
            return False




# class BinaryTreeNode:
#     def __init__(self, value):
#         self.value = value
#         self.left = left
#         self.right = right
#
#     def insert_left(self):
#         self.left = BinaryTreeNode.value
#         return self.left
#
#     def insert_right(self):
#         self.right = BinaryTreeNode.value
#         return self.right
