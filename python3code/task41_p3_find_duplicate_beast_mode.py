# https://www.interviewcake.com/question/python/find-duplicate-optimize-for-space-beast-mode
# We know the position of a node with multiple incoming pointers is a duplicate in our list because the nodes that pointed to it must have the same value.
# We find a node with multiple incoming pointers by finding the first node in a cycle.
# We find the first node in a cycle by finding the length of the cycle and advancing two pointers: one starting at the head of the linked list, and the other starting ahead as many steps as there are nodes in the cycle. The pointers will meet at the first node in the cycle.
# We find the length of a cycle by remembering a position inside the cycle and counting the number of steps it takes to get back to that position.
# We get inside a cycle by starting at the head and walking nn steps. We know the head of the list is at position n + 1n+1.

def find_duplicate(int_list):
    n = len(int_list) - 1

    # STEP 1: GET INSIDE A CYCLE
    # start at position n+1 and walk n steps to
    # find a position guaranteed to be in a cycle
    position_in_cycle = n + 1
    print("inside the cycle")
    # since we're looping in range from 0 to n we'll eventually end up in the loop (if duplicates
    # exist
    for _ in range(n):
        position_in_cycle = int_list[position_in_cycle - 1]
        # we subtract 1 from the current position to step ahead:
        # the 2nd *position* in a list is *index* 1

    # we found the position in the cylce position_in_cycle
    # STEP 2: FIND THE LENGTH OF THE CYCLE
    # find the length of the cycle by remembering a position in the cycle
    # and counting the steps it takes to get back to that position
    remembered_position_in_cycle = position_in_cycle
    current_position_in_cycle = int_list[position_in_cycle - 1]  # 1 step ahead
    cycle_step_count = 1

    while current_position_in_cycle != remembered_position_in_cycle:
        current_position_in_cycle = int_list[current_position_in_cycle - 1]
        cycle_step_count += 1

    # STEP 3: FIND THE FIRST NODE OF THE CYCLE
    # start two pointers
    #   (1) at position n+1
    #   (2) ahead of position n+1 as many steps as the cycle's length
    pointer_start = n + 1
    pointer_ahead = n + 1
    for _ in range(cycle_step_count):
        pointer_ahead = int_list[pointer_ahead - 1]

    # advance until the pointers are in the same position
    # which is the first node in the cycle
    while pointer_start != pointer_ahead:
        pointer_start = int_list[pointer_start - 1]
        pointer_ahead = int_list[pointer_ahead - 1]

    # since there are multiple values pointing to the first node
    # in the cycle, its position is a duplicate in our list
    return pointer_start

if __name__ == "__main__":
    l = [1, 2, 3, 4, 5, 5, 6, 7, 8]
    print(find_duplicate(l))
    # print(shuffle(l))
    # print(l)
    #
    # l = [1, 2, 3, 4, 5, 6, 7, 8]
    # z=find_repeat(l)
    # print(z,l[z])