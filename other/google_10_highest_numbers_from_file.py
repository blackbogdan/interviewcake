
# return 10 highest numbers in the file. Each line of the file represents one number. File is too big to fit in the
# memory
def ten_highest_numbers(filename):
    # this is how you can read file line by line
    top_10 = [None]*10
    count = 0
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            number = int(line)
            if count < 10:
                top_10[count] = number
                count += 1
                continue
            top_10.sort()
            if top_10[0] < number:
                top_10[0] = number
    return top_10



print(ten_highest_numbers("google_10_highest_file.txt"))