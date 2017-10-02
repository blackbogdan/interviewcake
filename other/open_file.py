
def print_content(filepath):
    with open(filepath) as handle:
        text = handle.read()
        print(text)
        text = text.split(" ")
    print(text)
        # lst = list(text)
    # print(lst)
print_content("unsorted.txt")