__author__ = 'bkapusta'
import random
# Binary tree explained (Joe James)
# https://www.youtube.com/watch?v=YlgPi75hIBc&index=7&list=PLj8W7XIvO93qsmdxbaDpIvM1KCyNO1K_c
#
# traversal explained:
# http://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
#          1
#         / \
#        2   3
#       / \
#      4   5

# Depth First Traversals:
#  Preorder (Root, Left, Right) : 1 2 4 5 3
#  Postorder (Left, Right, Root) : 4 5 2 3 1
#  Inorder (Left, Root, Right) : 4 2 5 1 3
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
    # recursive traversal function on the node class:
    def preorder(self):
        if self:
            # print value of the current node.
            # TO DO: why should we print as a string???
            # calling "if" statements instead of "elif" to make this consistent
            print self.value
            if self.leftChild:
                # if there's a left child, it calls the preorder on the left child
                self.leftChild.preorder()
            if self.rightChild:
                # if there's a left child, it calls the preorder on the right child
                self.rightChild.preorder()

    def postorder(self):
        if self:
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print self.value

    def inorder(self):
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print self.value
            if self.rightChild:
                self.rightChild.inorder()


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

    def preorder(self):
        print "PerOrder"
        self.root.preorder()

    def postorder(self):
        print "PostOrder"
        self.root.postorder()

    def inorder(self):
        print "InOrder"
        self.root.inorder()
# print [random.randint(1, 20) for i in range(11)]

# [17, 2, 6, 16, 6, 20, 4, 16, 18, 16, 11]
# this will build up a tree
#                       17
#                     /       \
#                    2         20
#                     \       /
#                      6     18
#                     /  \
#                    4    16
#                         /
#                        11

l = [17, 2, 6, 16, 6, 20, 4, 16, 18, 16, 11]
bst = Tree()
for item in l:
    bst.insert(item)
print "==="*6
bst.inorder()
print "==="*6
bst.postorder()
print "==="*6
bst.preorder()
print bst.find(20)
print bst.find(99)
