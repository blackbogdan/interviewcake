class Node:
    def __init__(self, d, n = None):
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
        this_node = self.root
        prev_node = None

        while this_node:
            if this_node.data == d:
                if prev_node:
                    prev_node.next_node = this_node.next_node
                else:
                    self.root = this_node
                self.size -= 1

            else:
                prev_node = this_node
                this_node = this_node.next_node
        return False

    def print_all(self):
        this_node = self.root
        while this_node:
            this_node = this_node.next_node