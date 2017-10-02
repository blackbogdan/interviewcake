from pprint import pprint
'''
I wrote a crawler that visits web pages, stores a few keywords
in a database, and follows links to other web pages.
I noticed that my crawler was wasting a lot of time visiting the same pages over and over,
so I made a set, visited, where I'm storing URLs I've already visited.
Now the crawler only visits a URL if it hasn't already been visited.

Thing is, the crawler is running on my old desktop computer in my parents' basement
(where I totally don't live anymore), and it keeps running out of memory because
visited is getting so huge.

How can I trim down the amount of space taken up by visited?
'''
'''
solution:
We can use a trie.
Let's make visited a nested dictionary where each map has keys of just one character.
So we would store 'google.com' as
visited['g']['o']['o']['g']['l']['e']['.']['c']['o']['m']['*'] = True.
The '*' at the end means 'this is the end of an entry'.
'''
class Trie:

    def __init__(self):
        # we're creating root node to store values
        self.root_node = {}

    def check_if_present_and_add(self, word):
        current_node = self.root_node
        is_new_word = False
        for char in word:
            if char not in current_node:
                is_new_word = True
                current_node[char] = {}
            current_node = current_node[char]

        if "End Of Word" not in current_node:
            is_new_word = True
            current_node["End Of Word"] = {}
        return is_new_word

s = Trie()
s.check_if_present_and_add("google.com")
s.check_if_present_and_add("google.com/about")
s.check_if_present_and_add("google.com/carrers")
s.check_if_present_and_add("google.com/carrers/qa")
s.check_if_present_and_add("google.com/carrers/dev")
s.check_if_present_and_add("google.com/carrers/sales")
# print s.root_node['g']['o']['o']['g']['l']['e']['.']['c']['o']['m']
print s.root_node['g']['o']['o']['g']['l']['e']['.']['c']['o']['m']["End Of Word"]
pprint(s.root_node)