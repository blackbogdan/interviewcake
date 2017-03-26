from task8_binary_tree_explained import Tree


def is_superbalanced(tree_root):
    # a tree with no nodes is superbalanced, since there're no leaves!
    if tree_root == None:
        return True

    depths = [] # we should short-circut as soon as we find more than 2

#     we'll treat this list as a stack that will store tuples of (node, depth)
#     because we're using "depth first search" approach
    nodes = []
    nodes.append((tree_root, 0))
    while len(nodes):
        # pop a node and it's depth from the top of our stack
        # Pop shall remove last item from the list
        node, depth = nodes.pop()
        # in case we found a leaf (it does not have left and right nodes)
        if (not node.left) and (not node.right):
            # we only care of it's a NEW depth
            if depth not in depths:
                depths.append(depth)
#            two ways we might now have an unbalanced tree:
#               1) more than 2 different leaf depths;
#               2) 2 leaf depths that are more than 1 apart.
                if (len(depths) > 2) or \
                        ((len(depths)) == 2 and abs(depths[0] - depths[1]) > 1):
                    return False
        # else it is NOT a Leaf - keep getting down!
        else:
            if node.left:
                nodes.append((node.left, depth + 1))
            if node.right:
                nodes.append((node.right, depth + 1))
    return True

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
# print is_superbalanced(bst)