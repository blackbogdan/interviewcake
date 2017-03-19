import random
# z =  ["{}".format(random.randint(0, 3)) for i in xrange(10)]
# y = "".join(z)
# print "before", z
# random.shuffle(z)
# print z
# m = random.sample(z, len(z))
# print "random sample", m

def shuffle_vovels(str):
    '''TASK: to shuffle vovels in the string. Vovels in the beginning of the string will go to the end.
    Vovles in the end of the string will go to the beginning
    so,
    mother->methor'''
    l_vovels = ['a', 'e', 'u', 'i', 'o', 'y']
    lst_str = list(str)
    print lst_str
    positions_list = []
    for index, item in enumerate(lst_str):
        if item in l_vovels:
            positions_list.append(index)
    print positions_list
    for i in range(len(positions_list)/2):
        print positions_list[i]
        lst_str[positions_list[i]], lst_str[positions_list[len(positions_list)-i-1]] = lst_str[positions_list[len(positions_list)-i-1]], lst_str[positions_list[i]],
    print lst_str
    print positions_list, "".join(lst_str)


shuffle_vovels("macucysino")