#http://stackoverflow.com/questions/642763/python-intersection-of-two-lists
# http://www.saltycrane.com/blog/2008/01/how-to-find-intersection-and-union-of/


lista = ["a%s" %x for x in range(10)]

listb = ["b%s" %x for x in range(10)]
listc = ["a%s" %x for x in range(10)]
a_and_b =['a0', 'a3', 'a2', 'a5', 'b0', 'b1', 'b2']
a = ['a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'banana']
missing_1_in_a = ['a0', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9']
empty = []
print "lista", lista
print "listb", listb
print "listc", listc
print "list a_and_b", a_and_b
print "a:", a
print "missing_1_in_a 1 missing element (a1):", missing_1_in_a
print '---------------------------------------------------------'
sorted(a, reversed)
# a= set(lista) & set(listc)
# print a
#how to find out mathing itmes in list:
def same_items(l1, l2):
    return set(l1).intersection(l2)
# print "These items from first list are in second one:", same_items(listb, a_and_b)

#copare t2 equal lists:
def compare_2_with_set(l1, l2):
    if set(l1) & set(l2):
        return True
    else:
        return False
# print "compared 2 lists with set: BROKEN", compare_2_with_set(a_and_b, lista)

#compare 2 lists with cmp() function
def compare_with_cmp(l1,l2):
    if l1==[] or l2 ==[]:
        print "empty list"
    print cmp(l1,l2)
# print "compared_with_cmp: returns 0 if lists exactly match, -1 if one of the element" \
#       "does not match====>"
compare_with_cmp(lista, listc) #equal lists
compare_with_cmp(a_and_b, a) #a_and_b contains some items from a and extra from b
compare_with_cmp(lista, a)   #a has extra element "banana, comparing to list b
compare_with_cmp(missing_1_in_a, a)
compare_with_cmp(empty, a)
a.sort(reverse=True)
print a
#compare 2 lists with for loop:
def with_for_loop(l1,l2):
    l1.sort(reverse=True)
    print type(l1)
    l2.sort(reverse=True)
    # for i in xrange(len(l2 if len(l1)> len(l2) else l1)):
    for i in xrange(len(l1)):
        if l1[i]!=l2[i]:
            return False
    return True
# print with_for_loop(a, listc)

print "_"*100
import cProfile
def compare_totally(l1, l2):
#len(l1)!= len(l2)
#len(l1)>len(l2)
#lenl2>lenl1
#at least one element is different than lists are not equal
    if len(l1)!=len(l2): return False
    l1.sort(reverse=True)
    l2.sort(reverse=True)
    for i in xrange(len(l1)):
        if l1[i]!=l2[i]:
            return False
    return True
# print compare_totally(lista, listc)

def miukaa(list1,list2):
    for i in range(len(list1)):
        print list1[i]
        print list2[i]
piukaaa = lambda list1, list2 : [list1[i]+list2[i] for i in range(len(list1))]
print piukaaa(lista, listc)
#compare lists with equal elements, and extra ones



#compare lists with missing element



#compare unsorted lists
