# coding=utf-8
'''
Write a function to check that a binary tree ↴ is a valid binary search tree

A binary search tree is a binary tree in which, for each node:
The node's value is greater than all values in the left subtree.
The node's value is less than all values in the right subtree.
BSTs are useful for quick lookups. If the tree is balanced, we can search for a given value in the tree in O(lgn) time.
                      50
                    /   \
                   30    80
                  /  \
                20    60
                This tree is not valid, since 60 is > 50, but it's in the left node.
'''
from task8_binary_tree_explained import Tree
# SOLUTION 1:
# We do a depth-first walk through the tree, testing each node for validity as we go.
# A given node is valid if it's greater than all the ancestral nodes it's in the right
# sub-tree of and less than all the ancestral nodes it's in the left-subtree of.
#  Instead of keeping track of each ancestor to check these inequalities, we just check
# the largest number it must be greater than (its lower_bound) and the smallest number
# it must be less than (its upper_bound).
def is_binary_search_tree1(tree_root):
    # start at the root, with an arbitrarily low lower bound
    # and an arbitrarily high upper bound
    node_and_bounds_stack = [(tree_root, -float('inf'), float('inf'))]

    # depth-first traversal:
    while len(node_and_bounds_stack):
        node, lower_bound, upper_bound = node_and_bounds_stack.pop()
        print node, lower_bound, upper_bound
        if (node.value <= lower_bound) or (node.value >= upper_bound):
            return False

        if node.leftChild:
            # this node must be less than the current node
            node_and_bounds_stack.append((node.leftChild, lower_bound, node.value))

        if node.rightChild:
            # this node must be greater than the current node
            node_and_bounds_stack.append((node.rightChild, node.value, upper_bound))
    # if none of the nodes were invalid, return true
    # (at this point we checked all the nodes)
    return True

def is_binary_search_tree2(tree_root, lower_bound = -float('inf'), upper_bound = float('inf')):
    if not tree_root:
        return True
    if (tree_root.value >= upper_bound or tree_root.value <= lower_bound):
        return False
    return is_binary_search_tree2(tree_root.leftChild, lower_bound, tree_root.value) \
        and is_binary_search_tree2(tree_root.rightChild, tree_root.value, upper_bound)

# [17, 2, 6, 16, 6, 20, 4, 16, 18, 16, 11]
# this will build up a tree
#                         17
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
print is_binary_search_tree1(bst.root)