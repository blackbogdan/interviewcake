from python3code.p3binarytree import Tree
def find_largest(root):
    # largest item would be in the right most position. It should not
    # have right nodes (because that's how binary tree is built)
    if root is None:
        raise Exception("Tree does not contain any values")
    if root.right:
        return find_largest(root.right)
    # current node does not have right nodes, then current value is the largest one
    return root.value

def find_second_largest(root):
    # verifying if thre're more than 2 nodes:
    if root is None or (root.right is None and root.left is None):
        raise Exception("Need at least 2 elements to find the second largest")
    current = root
    # in order to avoid building a stack, we're using for loop
    while current:
        # if left child exists and right child does not, then
        # second largest is in the left child
        if current.right.right is None and current.right.left is not None:
            print("Looking for second largest in the left node")
            return find_largest(current.right.left)

        # if node does not have neither right child, nor left child
        # then second largest is parent of the node
        if current.right.right is None and current.right.right is None:
            print("Second largest is the parent node")
            return current.value

        # we need to step one node down to find second largest value
        current = current.right
if __name__ == "__main__":
    # l = [17, 2, 6, 16, 6, 20, 4, 16, 18, 16, 11]
    # l = [17, 2, 6, 16, 6, 20, 4, 16, 18, 16, 11]
    l = [17, 2, 6, 16, 6, 20, 4, 16, 16, 11]
    l = [21, 25, 20]
    tr = Tree()
    z = Tree()
    for i in l:
        tr.insert(i)
    print("largest: %s" % find_largest(tr.root))
    print("second largest: %s" % find_second_largest(tr.root))

    # tr.postorder()
    #    17
    #    / \
    #   /   \
    #  /     \
    # 2      20
    #  \     /
    #   6   18
    #  / \
    # 4  16
    #    /
    #   11
    # print("largest node is: %s" % tr.find_largest())
    # print("largest node value is: %i" % tr.find_largest().value)
    #
    # tr.find_second_largest()
    # print(tr.find_smallest())
    # print(tr.find_largest())
    # print(z.find_largest())