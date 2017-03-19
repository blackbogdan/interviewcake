# coding=utf-8
# Suppose we could access yesterday's stock prices as a list, where:
#
# The indices are the time in minutes past trade opening time, which was 9:30am local time.
# The values are the price in dollars of Apple stock at that time.
# So if the stock cost $500 at 10:30am, stock_prices_yesterday[60] = 500.
#
# Write an efficient function that takes stock_prices_yesterday and returns the best profit I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday.
# stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
#
# get_max_profit(stock_prices_yesterday)
# returns 6 (buying for $5 and selling for $11)
#
import time


# stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
stock_prices_yesterday = [12, 11, 10, 9, 7, 4]
def get_max_profit1(stock_prices_yesterday):
    "BRUTE FORCE APPROACH"
    '''
    the point of this code is to find maximum porfit by comparing existing one
    in the beginning of the for loop to max_profit
    '''

    max_profit = 0

    # go through every time
    start_time = time.time()
    time.sleep(1)
    for outer_time in xrange(len(stock_prices_yesterday)):

        # for every time, go through every OTHER time
        for inner_time in xrange(len(stock_prices_yesterday)):
            # for each pair, find the earlier and later times
            earlier_time = min(outer_time, inner_time)
            later_time = max(outer_time, inner_time)

            # and use those to find the earlier and later prices
            earlier_price = stock_prices_yesterday[earlier_time]
            later_price   = stock_prices_yesterday[later_time]

            # see what our profit would be if we bought at the
            # earlier price and sold at the later price
            potential_profit = later_price - earlier_price

            # update max_profit if we can do better
            max_profit = max(max_profit, potential_profit)
    print("--- %s seconds ---" % (time.time() - start_time))
    return max_profit

def get_max_profit2(stock_prices_yesterday):
    "STILL BRUTE FORCE, but better one"

    max_profit = 0

    # go through every price (with its index as the time)
    for earlier_time, earlier_price in enumerate(stock_prices_yesterday):
        print earlier_time, earlier_price
        # and go through all the LATER prices
        for later_price in stock_prices_yesterday[earlier_time+1:]:
            print "==============="
            print stock_prices_yesterday[earlier_time+1:]
            # see what our profit would be if we bought at the
            # earlier price and sold at the later price
            potential_profit = later_price - earlier_price

            # update max_profit if we can do better
            max_profit = max(max_profit, potential_profit)

    return max_profit

def get_max_profit3(stock_prices_yesterday):
    """A greedy algorithm iterates through the problem space taking
     the optimal solution "so far," until it reaches the end.
    The greedy approach is only optimal if the problem has "optimal substructure,"
    which means stitching together optimal solutions to subproblems yields an optimal solution"""

    min_price = stock_prices_yesterday[0]
    max_profit = 0
    for current_price in stock_prices_yesterday:
        # ensure min_price is the lowest price we've seen so far

        min_price = min(min_price, current_price)

        # see what our profit would be if we bought at the
        # min price and sold at the current price
        potential_profit = current_price - min_price

        # update max_profit if we can do better
        max_profit = max(max_profit, potential_profit)

    print max_profit

""" Let’s think about some edge cases. What if the stock value stays the same? What if the stock value goes down all day?
first scenario is good, what about second one"""




# stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
stock_prices_yesterday = [12, 13, 10, 9, 7, 4]
def get_max_profit3(stock_prices_yesterday):
    # make sure we have at least 2 prices
    if len(stock_prices_yesterday) < 2:
        raise IndexError('Getting a profit requires at least 2 prices')

    # we'll greedily update min_price and max_profit, so we initialize
    # them to the first price and the first possible profit
    min_price = stock_prices_yesterday[0]
    max_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]

    for index, current_price in enumerate(stock_prices_yesterday):

        # skip the first (0th) time
        # we can't sell at the first time, since we must buy first,
        # and we can't buy and sell at the same time!
        # if we took this out, we'd try to buy /and/ sell at time 0.
        # this would give a profit of 0, which is a problem if our
        # max_profit is supposed to be /negative/--we'd return 0!
        if index == 0:
            continue

        # see what our profit would be if we bought at the
        # min price and sold at the current price
        potential_profit = current_price - min_price

        # update max_profit if we can do better
        max_profit = max(max_profit, potential_profit)

        # update min_price so it's always
        # the lowest price we've seen so far
        min_price = min(min_price, current_price)

    print max_profit

get_max_profit3(stock_prices_yesterday)



















