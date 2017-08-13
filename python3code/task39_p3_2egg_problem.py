# https://www.interviewcake.com/question/python/two-egg-problem
# A building has 100 floors. One of the floors is the highest floor an egg can be dropped
# from without breaking.If an egg is dropped from above that floor, it will break. If it
# is dropped from that floor or below, it will be completely undamaged and you can drop the egg again.
#
# Given two eggs, find the highest floor an egg can be dropped from without
# breaking, with as few drops as possible.

# approach to this problem:
# If we had 1 egg, we would go from bottom to the top dropping it to figure out what's the highest floor.
# This would give us O(n) coplexity
# However, we have 2 eggs.
# We could use binary approach, with worst case of 50 drops (1 to determine range, 49 to determine number within
# that range)
# Maybe we can skip less?
# what if we skip 10 floors at a time? Then worst case would be the 100-th floor, which is 10 drops plus
# 9 drops from 91 till 99 (including 99). Thus makes it 10+9=19 drops.
#
# What if the building changes to 1000 floors, then this algorithm needs to be adjusted. Additionally,
# maybe we could improve worst case to even less drops. What if number of drops would be dependant from
# number of floors?
# What if We decrease number of drops each time? Then, By reaching top floor, we would need to use less drops.
# However, in the first step we would need to skip more.
# If n is number of skipped floors, then we have equasion:
#     n + (n-1) + (n-2) + ... +1 = 100
# This is a TRIANGLE series!
# A triangular series always starts with 1 and increases by 1 with each number.
# Sum of fist and last, second first and second last is always contant. For example:
# Total sum =15, n = 5, because 1+2+3+4+5==15
# 1+5=6
# 2+4=6
# 3+3=6
# SO, This is true for every triangular series:
# 1) Pairs of numbers on each side will always add up to the same value.
# 2) That value will always be 1 more than the series’ n.
#
# PATTERN: Each pairs sum is (n+1). Total number of pairs is n/2 rounded to higher value.
# in our example, n = 5. n+1==6. Sum of pairs is n/2 = 5/2 = 2.5=3


# in the end of the day our equation is: (n+1)*n/2. Or (n**2 + n)/2=15 (or 100 in case with the building
# n**2 + n - 200 = 0
# n = (-b +-sqrt(b**2-4ac))/2a
# n1 = (-1 + sqrt(1**2 - 4*1*(-200)))/2*1
# n1 = (-1 + 28.302)/2=13.65 which is approx 14
# n2 is, obviously, a negative number, which doesn't fit our task
# So we skip in first time 14 floors, second time 14-1, third time 14-2 and so on until we reach 100-th floor.
# after we determine the range, we'll drop second egg from previous range to the current one
# Let's Look at 2 cases:
# ==========================FIrst case:
# Highest floor an egg won't break from
# 13
#
# Floors we drop first egg from
# 14
#
# Floors we drop second egg from
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13
#
# Total number of drops
# 14
#
# ==========================Second Case
# Highest floor an egg won't break from
# 98
#
# Floors we drop first egg from
# 14, 27, 39, 50, 60, 69, 77, 84, 90, 95, 99
#
# Floors we drop second egg from
# 96, 97, 98
#
# Total number of drops
# 14

