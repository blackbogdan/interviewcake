import json
import re
from collections import Counter
def count_words_files(file="unsorted.txt"):
    with open(file, 'r') as f:
        counts={}
        text = f.read()
        words=text.split()
        print words
        for word in words:
            word=word.lower()
            if ',' in word: word=word[:-1]
            counts[word]=counts.get(word,0)+1
        keys=counts.keys()
        values=counts.values()

        print keys[values.index(max(values))], max(values)
count_words_files()

def count_keys_in_json(json_file="json_example.json"):
    with open(json_file) as handle:
        counted_keys={}
        text = handle.read()
        y = json.loads(text)
        z = Counter(y['menu'])
        for item in y['menu']:

            counted_keys[item] =counted_keys.get(item,0)+1
            print y['menu'][item]
        print "Yo mama counted keys", counted_keys
# count_keys_in_json()
def element_in_json(json_file="json_example.json", key_to_find="id"):
    with open(json_file) as handle:
        counted_keys={}
        counted_values = {}
        text = handle.read()
        y = json.loads(text)
        for item in y['menu']:

            # print y['menu'][item]
            for elem in y['menu'][item]:
                if elem == None or type(elem)==unicode: continue
                for value in elem.values():
                    counted_values[value] = counted_values.get(value,0) + 1
                for key in elem.keys():
                    counted_keys[key]=counted_keys.get(key, 0)+1
        print "Nubmers of used keys:", counted_keys
        list_of_frequently_used_keys = counted_keys.keys()
        list_of_frequently_used_values = counted_keys.values()


        print "Most frequent used key is: {0}. Number of occurences is {1}.".format(list_of_frequently_used_keys[
                                                                                list_of_frequently_used_values.index(
                                                                                max(list_of_frequently_used_values)
        )], max(list_of_frequently_used_values))
        print counted_values
element_in_json()