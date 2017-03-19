def change_possibilities_bottom_up(amount, denominations):
    ways_of_doing_n_cents = [0] * (amount + 1)
    print ways_of_doing_n_cents
    ways_of_doing_n_cents[0] = 1
    print ways_of_doing_n_cents

    for coin in denominations:
        print "===============>Calulating coin: ", coin
        for higher_amount in xrange(coin, amount + 1):
            print "higher amount is: %i" % (higher_amount)
            higher_amount_remainder = higher_amount - coin
            print "higher_amount_remainder", higher_amount_remainder
            ways_of_doing_n_cents[higher_amount] += ways_of_doing_n_cents[higher_amount_remainder]
            print "Ways of doing n cents", ways_of_doing_n_cents
            print "______________"*5

    return ways_of_doing_n_cents[amount]
print change_possibilities_bottom_up(4, [1,2,3])


def change_possibilities_top_down(amount_left, denominations, current_index=0):
    # base cases:
    # we hit the amount spot on. yes!
    if amount_left == 0: return 1

    # we overshot the amount left (used too many coins)
    if amount_left < 0: return 0
    
    # we're out of denominations
    if current_index == len(denominations): return 0

    print "checking ways to make %i with %s. Current index: %s" % (amount_left, denominations[current_index:], current_index)

    # choose a current coin
    current_coin = denominations[current_index]

    # see how many possibilities we can get
    # for each number of times to use current_coin
    num_possibilities = 0
    while amount_left >= 0:
        num_possibilities += change_possibilities_top_down(amount_left, denominations, current_index + 1)
        print "yo mama al = %i, c_c = %i, c_i=%i " % (amount_left, current_coin, current_index)
        amount_left -= current_coin

    return num_possibilities


print change_possibilities_top_down(4, [1,2,3])


class Change:
    def __init__(self):
        self.memo = {}

    def change_possibilities_top_down(self, amount_left, denominations, current_index=0):

        # check our memo and short-circuit if we've already solved this one
        memo_key = str((amount_left, current_index))
        if memo_key in self.memo:
            print "grabbing memo[%s]" % memo_key
            return self.memo[memo_key]

        # base cases:
        # we hit the amount spot on. yes!
        if amount_left == 0: return 1

        # we overshot the amount left (used too many coins)
        if amount_left < 0: return 0

        # we're out of denominations
        if current_index == len(denominations): return 0

        print "checking ways to make %i with %s" % (amount_left, denominations[current_index:])

        # choose a current coin
        current_coin = denominations[current_index]

        # see how many possibilities we can get
        # for each number of times to use current_coin
        num_possibilities = 0
        while amount_left >= 0:
            num_possibilities += self.change_possibilities_top_down(amount_left, denominations, current_index + 1)
            amount_left -= current_coin

        # save the answer in our memo so we don't compute it again
        self.memo[memo_key] = num_possibilities
        return num_possibilities

# print Change().change_possibilities_top_down(4, [1, 2, 3])