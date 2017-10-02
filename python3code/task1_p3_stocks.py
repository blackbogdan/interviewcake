# coding=utf-8
# Suppose we could access yesterday's stock prices as a list, where:
#
# The indices are the time in minutes past trade opening time, which was 9:30am local time.
# The values are the price in dollars of Apple stock at that time.
# So if the stock cost $500 at 10:30am, stock_prices_yesterday[60] = 500.
#
# Write an efficient function that takes stock_prices_yesterday and returns the best profit I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday.
stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
#
# get_max_profit(stock_prices_yesterday)
# returns 6 (buying for $5 and selling for $11)
# stock_prices_yesterday = [12, 11, 10, 9, 7, 4]

def get_max_profit(lst):
    # at this point I'll assume that all items in the list are integers
    if len(lst)<2:
        raise ValueError("You need more than 2 prices to calculate a profit")

    # we could brute force it, but maybe there's a better solution?
    # how about "Greedy" approach
    # we shall walk through the list calculating the profit and
    # storing the maximum profit "so far"
    # for that we'll need maxim price and minimum price so far as well
    max_profit = lst[1] - lst[0]
    # got the profit
    min_price = lst[0]
    for index, current_price in enumerate(lst):
        if index == 0:
            continue
        potential_profit = current_price - min_price
        max_profit = max(potential_profit, max_profit)
        min_price = min(current_price, min_price)

    return max_profit
print(stock_prices_yesterday)
print(get_max_profit(stock_prices_yesterday))
print(get_max_profit([1, 2]))
print(get_max_profit([2, 1]))