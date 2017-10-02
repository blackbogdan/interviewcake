__author__ = 'bkapusta'


def contains_cycle(first_node):
    slow_runner = first_node
    fast_runner = first_node
    while slow_runner != fast_runner and fast_runner.next_node is not None:
        slow_runner = slow_runner.next_node
        fast_runner = fast_runner.next_node.next_node
        if fast_runner == slow_runner:
            return True
    return False
