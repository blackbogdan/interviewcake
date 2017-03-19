##http://stackoverflow.com/questions/20672238/find-dictionary-keys-with-duplicate-values

d1 = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
d2 = {'z': 260, 'd': -12, 'r': 1, 'b': 0}

dv0 = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
dv1 = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
dv2 = {'a': 10, 'b': 5, 'c': 87, 'd': 40}
dvbig = {'a': 10, 'b': 6, 'c': 87, 'm':16, 'd': 40}


dk0 = {'a': 10, 'buka': 20, 'c': 30, 'dodo': 40}
dk1 = {'a': 10, 'buka': 20, 'c': 30, 'dodo': 40}
dk2 = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
dk_no_dup = {'a': 10, 'bkb': 20, 'c': 30, 'domain': 40, 'extra': 50, 'nobhill_foods':60}
dk_with_dup = {'a': 10, 'bkb': 20, 'c': 30, 'domain': 40, 'extra': 20, 'nobhill_foods':20}
#known keys with different values
def are_diff_values(d1, d2):
    for k, v in d1.iteritems():
        if KeyError: continue
        if not v==d2[k]:
            print "dict1: %s: %s. Dict2 %s: %s" %(k, d1[k], k, d2[k])
#known values with different keys:


# dv3 = {k:v for k,v in dvbig.iteritems() if dvbig[k]!=dv1[k] if not KeyError}
# print  dv3
#
print are_diff_values(dvbig, dv2)


#known values with different keys:
some_dict = {"firstname":"Albert","nickname":"Albert","surname":"Likins","username":"Angel"}
# >>> rev_multidict = {}
# >>> for key, value in some_dict.items():
# ...     rev_multidict.setdefault(value, set()).add(key)
def static_values_dynamic_keys(d1, d2):
    extra_keys_from_fist_dict = {}
    rev_multidict={}
    print "d1 original: ", d1
    print "d2 oridingal:", d2
    print "--"*39

    '''
    dict.get never raises keyerror
    '''

    flipped_d1 = {v:k for k,v in d1.items()}

    flipped_d2 = {v:k for k,v in d2.items()}
    # print "flipped", flipped_d
    # for k, v in some_dict.items():
    #     rev_multidict.setdefault(v, []).append(k)
    print "flipped_d1:", flipped_d1
    print "flipped_d2:", flipped_d2
    for k, v in flipped_d1.items():
        # rev_multidict.setdefault(k, []).append(flipped_d1[k])
        # rev_multidict.setdefault(k, []).append(flipped_d1[k])
        try:
            rev_multidict.setdefault(k, set()).add(flipped_d2[k])
            rev_multidict.setdefault(k, set()).add(flipped_d1[k])
        except KeyError:
            extra_keys_from_fist_dict.setdefault(k, []).append(flipped_d1[k])
            print "found extra key"
    duplicates={k:list(v) for k,v in rev_multidict.items() if len(v)>1}
    print "duplicates", duplicates
    print rev_multidict
    print extra_keys_from_fist_dict
    print "="*100
    print "="*100
    print "\n"

# static_values_dynamic_keys(dk1, dk2)
# static_values_dynamic_keys(dk2, dk1)
# static_values_dynamic_keys(dk2, dk_no_dup)
# static_values_dynamic_keys(dk_no_dup, dk2)
# static_values_dynamic_keys(dk_with_dup, dk2)
# static_values_dynamic_keys(dk2, dk_with_dup)

def compare_with_deletion_first(d_or, d2):
    print d_or
    print d2
    build_from_or = {}
    for k, v in d_or.iteritems():
        if k not in d2:
            build_from_or[k] = v
            continue
        else:
            print k, v
            del d2[k]
    print build_from_or
    print d2
    print "="*100

compare_with_deletion_first(dk1, dk2)
compare_with_deletion_first(dk_with_dup, dk2)
