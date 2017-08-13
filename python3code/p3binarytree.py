class Node:
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.value == data:
            return False
        elif data < self.value:
            if self.left:
                return self.left.insert(data)
            else:
                self.left = Node(data)
                return True

        elif data > self.value:
            if self.right:
                return self.right.insert(data)
            else:
                self.right = Node(data)
                return True

    def find(self, data):
        if self.value == data:
            return True
        elif data < self.value:
            if self.left:
                return self.left.find(data)
            else:
                return False
        elif data > self.value:
            if self.right:
                return self.right.find(data)
            else:
                return False

    def preorder(self):
        if self:
            print(self.value)
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()

    def inorder(self):
        if self:
            if self.left:
                self.left.inorder()
            print(self.value)
            if self.right:
                self.right.preorder()

    def postorder(self):
        if self:
            if self.left:
                self.left.postorder()
            if self.right:
                self.right.postorder()
            print(self.value)

    def find_largest(self):
        if self.right:
            # print('1')
            # print(self.value)
            # print(self.right.value)
            return self.right.find_largest()
        # print("largest value is {}".format(self.value))
        return self

    def find_smallest(self):
        if self.left:
            return self.left.find_smallest()
        return self.value


    # def find_second_largest(self):
    #     if self.
class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
            return True
        else:
            return self.root.insert(data)

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def preorder(self):
        print("PreOrder")
        self.root.preorder()

    def inorder(self):
        print("InOrder")
        self.root.inorder()

    def postorder(self):
        print("PostOrder")
        self.root.postorder()

    def find_largest(self):
        # initiate the find largest
        if self.root:
            return self.root.find_largest()
        # there're no items in tree
        else:
            raise Exception("Tree is empty")

    def find_smallest(self):
        if self.root:
            return self.root.find_smallest()
        else:
            raise Exception("Tree is empty")

    def find_second_largest(self):
        if (self.root is None) or (self.root.right is None and self.root.left is None):
            raise Exception("Root has less than 2 elements, which makes it impossible to find \
                            second largest item")
#         if we have left child of the largest element, then second largest would be there
        largest_node = self.find_largest()
        # in case left node is not none
        if largest_node.left is not None:
            print("Yes, left child is not none, looking for largest Node")
            print(largest_node.left.find_largest().value)
        else:
            print(largest_node.value)
            print("it must be in the parent node")
if __name__ == "__main__":
    l = [17, 2, 6, 16, 6, 20, 4, 16, 18, 16, 11]
    l = [17, 2, 6, 16, 6, 20, 4, 16, 16, 11, 19]
    tr = Tree()
    for i in l:
        tr.insert(i)
    tr.preorder()
    tr.postorder()
    tr.inorder()
    print(tr.find(20))
    print(tr.find(30))