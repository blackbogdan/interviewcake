("weight, kg", "value, pounds ")
cake_tuples = [(7, 160), (3, 90), (2, 15)]

capacity1 = 20
# max_duffel_bag_value(cake_tuples, capacity)
# returns 555 (6 of middle type of cake and 1 of the last type of cake)

def max_value(tuples, capacity):
    print("=="*40)
    print("List of tuples: ", tuples)
    print("Bag capacity: ", capacity)
    # let's allocate list that will store monetary values of each cake
    # capacity + 1, because first capacity would be at index 0 and last one would
    # be at index capacity
    max_values_at_capacities = [0]*(capacity + 1)
    print(max_values_at_capacities)
    print(len(max_values_at_capacities))
    for current_capacity in range(capacity +1):
        #maximum monetary value so far
        current_max_value = 0
        for cake_weight, cake_value in tuples:
            # this handles 0 cases when bag capacity is 0 and cake weight is 0
            if (cake_weight == 0 and cake_value != 0):
                return float('inf')
            #should we use this particular cake for current capacity or not?
            # if cake doesn't fit in current_capacity, then we skip it
            if cake_weight <= current_capacity:
                # let's calculate maximum value for current capacity
                # we take current cake value and add to it maximum value from previously calculated capacities
                # for example, if current cake is (8, 14) and current capacity is 10:
                # we would take 14 and add to it value that was calculated for weight=current_capacity - cake_weigight
                # which is weight = 10 -8 =2
                max_value_using_cake = cake_value + max_values_at_capacities[current_capacity - cake_weight]

                # we update current max value
                current_max_value = max(current_max_value, max_value_using_cake)

            max_values_at_capacities[current_capacity] = current_max_value
    print(max_values_at_capacities)

    return max_values_at_capacities[capacity]

if __name__=="__main__":
    print(max_value(cake_tuples, capacity1))
    print(max_value([(1, 10), (2, 33)], 5))
    print(max_value([(1, 10), (2, 33)], 4))