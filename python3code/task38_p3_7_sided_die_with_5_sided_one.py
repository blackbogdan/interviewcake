from random import randint
def ran():
    return randint(1,5)


def rand7():
    while True:
        roll1 = ran()
        roll2 = ran()
        outcome_number = (roll1 - 1)*5 + (roll2 - 1) + 1
        print(outcome_number)
        if outcome_number == 7 or outcome_number == 1:
            break
        if outcome_number > 21:
            continue
        return outcome_number % 7 + 1

def rand7_table():

    results = [
        [1, 2, 3, 4, 5],
        [6, 7, 1, 2, 3],
        [4, 5, 6, 7, 1],
        [2, 3, 4, 5, 6],
        [7, 0, 0, 0, 0],
    ]

    while True:

        # do our die rolls
        row = rand5() - 1
        column = rand5() - 1

        # case: we hit an extraneous outcome
        # so we need to re-roll
        if row == 4 and column > 0:
            continue

        # our outcome was fine. return it!
        return results[row][column]


if __name__ == "__main__":
    # for i in range(10):
    #     print(randint(1, 5))
    print(rand7())