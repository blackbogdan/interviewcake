class Node:
    def __init__(self, d, n = None, p=None):
        self.data = d
        self.next_node = n
        self.prev_node = p

class d_linked_list:
    def __init__(self, r = None):
        self.root = r
        self.size = 0

    def add(self, d):
        new_node = Node(d, self.root)
        if self.root:
            self.root.prev_node = new_node
        self.root = new_node
        self.size += 1

    def print_prev_cur_next(self):
        this_node = self.root
        while this_node:

            if this_node.prev_node:
                print "previous node: {}".format(this_node.prev_node.data)
            else:
                print "previous node is the root node"
            print "current node: {}".format(this_node.data)
            if this_node.next_node:
                print "next node: {}".format(this_node.next_node.data)
            else:
                print "next node is the last node"
            print "=="*20
            this_node = this_node.next_node

    def print_from_start(self):
        this_node = self.root
        while this_node:
            print this_node.data
            this_node = this_node.next_node

    def print_from_end(self):
        # question how to define last node to loop from?
        # without looping through the list. (I have list size, though)
        last_node = "something"
        while last_node:
            print last_node.data
            last_node = last_node.prev_node

    def remove(self, d):
        this_node = self.root
        while this_node:
            if this_node.data == d:
                next_n = this_node.next_node
                prev_n = this_node.prev_node
                # if next node exists (not None)
                if next_n:
                    next_n.prev_node = prev_n
                # if previous node exists (not None)
                if prev_n:
                    prev_n.next_node = next_n
                else:
                    # this will happen if the
                    self.root = next_n
                self.size -= 1
                return True
            else:
                this_node = this_node.next_node
        return False
my_list = d_linked_list()
my_list.add(12)
my_list.add(13)
my_list.add(110)
# my_list.print_prev_cur_next()

my_list.print_from_start()
print my_list.remove(82)
print "=="*20
my_list.print_from_start()