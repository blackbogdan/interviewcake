class Node:
    def __init__(self, d, n=None):
        self.data = d
        self.next_node = n

class LinkedList:
    def __init__(self, r = None):
        self.root = r
        self.size = 0

    def add(self, d):
        new_node = Node(d, self.root)
        self.root = new_node
        self.size += 1

    def find(self, d):

        this_node = self.root
        while this_node:
            if this_node.data == d:
                return d
            else:
                this_node = this_node.next_node
        return False

    def remove(self, d):
        # set the root node as beginning of search
        this_node = self.root
        prev_node = None
        # loop through the linked list until this_node == None
        # that will happen when we reached the end of the linked list
        while this_node:
            # if we found the item
            if this_node.data == d:
                # we found the item and it's in the middle of the list
                # (not the first (self.root item). ==> it has previous
                # node which is not none
                if prev_node:
                    # print "setting pointers"
                    prev_node.next_node = this_node.next_node
                else:
                    self.root = this_node
                self.size -= 1
                return True #data was removed
            else:
                prev_node = this_node
                this_node = this_node.next_node
        return False #we did not find the item in list
    def print_all(self):
        this_node = self.root
        print "asdf",this_node.data
        while this_node:
            print this_node.data
            this_node = this_node.next_node

    def make_linked_list_looped(self):
        this_node = self.root
        while this_node:
            if this_node.next_node is None:
                this_node.next_node = self.root
                break
            this_node = this_node.next_node

if __name__ == "__main__":
    My_list = LinkedList()
    My_list.add(4)
    My_list.add(4)
    My_list.add(5)
    My_list.add(1)
    My_list.add(12)
    My_list.remove(5)
    print "size of the list: ", My_list.size
    # print My_list.print_all()
    My_list.make_linked_list_looped()
    My_list.print_all()