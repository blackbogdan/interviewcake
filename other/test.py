import random

import pprint
# z =  ["{}".format(random.randint(0, 3)) for i in xrange(10)]
# y = "".join(z)
# print "before", z
# random.shuffle(z)
# print z
# m = random.sample(z, len(z))
# print "random sample", m
# m = random.choice("asldfkjsdf")
# print m
# values = [random.randint(1,4) for i in range(1,11)]
# keys = [random.choice("asldfkjsdf") for i in xrange(1,11)]
# print keys, values
# d = zip(keys, values)
# print dict(d)
# print d


from datetime import datetime
d = datetime.strptime("19:00:55", "%H:%M:%S")
print d.minute
print type(d.hour)
print d.second