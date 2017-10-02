cake_tuples = [(7, 160), (3, 90), (2, 15)]

capacity1 = 20

def max_monetay_value(cake_tuples, bag_capacity):
    # allocate list which will represent max_monetay value of all capacities up to and including desired one:
    list_capacities = [0]*(bag_capacity + 1)

    for current_capacity in range(bag_capacity +1):

        current_max_value = 0
        for weight, value in cake_tuples:

            if current_capacity>=weight:
                # print(bag_capacity)
                # print(weight)
                max_value = value + list_capacities[current_capacity - weight]
                current_max_value=max(current_max_value, max_value)
        list_capacities[current_capacity]=current_max_value
    print(list_capacities)
    return list_capacities[bag_capacity]
print(max_monetay_value(cake_tuples, capacity1))