# coding=utf-8
"""You decide to test if your oddly-mathematical heating company is fulfilling its All-Time Max, Min, Mean and Mode Temperature Guarantee™.
Write a class TempTracker with these methods:

insert()—records a new temperature
get_max()—returns the highest temp we've seen so far
get_min()—returns the lowest temp we've seen so far
get_mean()—returns the mean ↴ of all temps we've seen so far (sum of all devided by number of inputs)
get_mode()—returns a mode ↴ of all temps we've seen so far
Optimize for space and time. Favor speeding up the getter functions (get_max(), get_min(), get_mean(), and get_mode()) over speeding up the insert() function.

get_mean() should return a float, but the rest of the getter functions can return integers.
 Temperatures will all be inserted as integers. We'll record our temperatures in Fahrenheit,
 so we can assume they'll all be in the range 0..1100..110.

If there is more than one mode, return any of the modes."""


class TempTracker:
    def __init__(self):
        self.min_temp = None
        self.max_temp = None
        # for mean
        self.mean = None
        self.sum_of_temp = 0.0
        self.count_of_inputs = 0
        #     for mode: # list of 0s at indices 0..110
        self.occurences = [0] * 111
        print self.occurences
        self.max_occurences = 0
        self.mode = None

    def insert(self, temperature):

        self.sum_of_temp += temperature
        self.count_of_inputs += 1
        if (self.max_temp is None) or (temperature > self.max_temp):
            self.max_temp = temperature
        if (self.min_temp is None) or (temperature < self.min_temp):
            self.min_temp = temperature
        self.occurences[temperature]+=1
        if self.occurences[temperature] >self.max_occurences:
            self.mode = temperature
            self.max_occurences = self.occurences[temperature]

    def get_max(self):
        return self.max_temp

    def get_min(self):
        return self.min_temp

    def get_mean(self):
        self.mean = self.sum_of_temp / self.count_of_inputs
        return self.mean

temp_tracker = TempTracker()
temp_tracker.insert(10)
temp_tracker.insert(19)
temp_tracker.insert(19)
temp_tracker.insert(9)
temp_tracker.insert(19)
temp_tracker.insert(15)
temp_tracker.insert(14)
print temp_tracker.max_temp
print temp_tracker.min_temp
print temp_tracker.get_mean()
print temp_tracker.mode
print temp_tracker.occurences