class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

    def insert(self, data):
        if self.value == data:
            return False
        elif self.value > data:
            if self.left:
                return self.left.insert(data)
            else:
                self.left = Node(data)
                return True
        elif self.value < data:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data)
                return True
    def find(self, data):
        if self.value == data:
            return True

        elif self.value > data:
            if self.left:
                return self.left.find(data)
            else:
                return False
        elif self.value < data:
            if self.right:
                return self.right.find(data)
            else:
                return False
    def preorder(self):
        if self:
            print self.value
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()
    def inorder(self):
        if self:
            if self.left:
                self.left.inorder()
            print self.value
            if self.right:
                self.right.inorder()
    def postorder(self):
        if self:
            if self.left:
                self.left.postorder()
            if self.right:
                self.right.postorder()
            print self.value




class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            # root does not exist:
            self.root = Node(data)
            return True
    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False
    def preorder(self):
        print "PreOrder"
        self.root.preorder()
    def inorder(self):
        print "InOrder"
        self.root.inorder()
    def postorder(self):
        print "PostOrder"
        self.root.postorder()

l = [17, 2, 6, 16, 6, 20, 4, 16, 18, 16, 11]
# l = [17, 2, 6, 16, 6, 20, 4, 16, 18, 16]
bst = Tree()
for item in l:
    bst.insert(item)
# print bst.find(3)
# bst.preorder()
# bst.inorder()
# bst.postorder()

def is_superbalanced(tree_root):
    if tree_root == None:
        return True
    depths = []
    nodes = []
    nodes.append((tree_root, 0))
    while len(nodes):
        node, depth = nodes.pop()

        if (not node.left) and (not node.right):
            # we only care if it's a new node
            if depth not in depths:
                print "we found a leaf!!! {}. Depth of the leaf: {}".format(node.value, depth)
                print "Depths: {}".format(depths)
                depths.append(depth)
                if len(depths)==2:
                    print "Lenth of depth ==2", abs(depths[0]-depths[1])
                    print depths[0]
                    print depths[1]

                if len(depths)>2 or \
                        (len(depths)==2 and abs(depths[0]-depths[1])>1):
                    print "Inside 'False' condition"
                    print depths
                    return False
        else:
            if node.left:
                nodes.append((node.left, depth + 1))
            if node.right:
                nodes.append((node.right, depth + 1))
    return True
print is_superbalanced(bst.root)