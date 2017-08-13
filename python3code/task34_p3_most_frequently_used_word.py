class WorldCloudData:
    def __init__(self, input_string):
        self.words_to_counts = {}
        self.populate_words_to_counts(input_string)

    def populate_words_to_counts(self, input_string):
        # iterates over the string, splitting it into words and passing those into add_word_to_dictionary()

        current_word_start_index = 0
        current_word_lenght = 0

        for i, character in enumerate(input_string):
            # if we reached the end of the string, we check if the last
            # character is a letter and add the last word to dictionary

            if i == len(input_string) - 1:
                if character.isalpha():
                    current_word_lenght += 1
                if current_word_lenght > 0:
                    current_word = input_string[current_word_start_index:
                        current_word_start_index + current_word_lenght]
                    self.add_word_to_dictionary(current_word)

            # if we reach a space or emdash we know we're at the end of a word
            # so we add it to our dictionary and reset our current word
            elif character == ' ' or character == u'\u2014':
                if current_word_lenght > 0:
                    current_word = input_string[current_word_start_index:
                                   current_word_start_index + current_word_lenght]
                    self.add_word_to_dictionary(current_word)
                    current_word_lenght = 0

            # we want to make sure we split on ellipses, so if we get two periods in a row,
            # we add the current word to our dictionary and reset our current word
            elif character == '.':
                if i < len(input_string) - 1 and input_string[i+1] == '.':
                    if current_word_lenght > 0:
                        current_word = input_string[current_word_start_index:
                                       current_word_start_index + current_word_lenght]
                        self.add_word_to_dictionary(current_word)
                        current_word_lenght = 0

            # if the character is a letter or an apostrophe, we add it to our current word
            elif character.isalpha() or character == '\'':
                if current_word_lenght == 0:
                    current_word_start_index = i
                current_word_lenght += 1

            # if the character is a hyphen, we want to check if it's surrounded by letters.
            # if it is, we add it to our current word
            elif character == '-':
                if i > 0 and input_string[i - 1].isalpha() and input_string[i + 1].isalpha():
                    if current_word_lenght == 0:
                        current_word_start_index == i
                    current_word_lenght += 1
                else:
                    if current_word_lenght > 0:
                        current_word = input_string[current_word_start_index:
                                       current_word_start_index + current_word_lenght]
                        self.add_word_to_dictionary(current_word)
                        current_word_lenght = 0

    def add_word_to_dictionary(self, word):
        # if the word in the dictionary we increment its count
        if word in self.words_to_counts:
            self.words_to_counts[word] += 1

        # if a lowercase version is in the dictionary, we know our input word must be uppercase
        # but we only include uppercase words if they're always uppercase
        # so we just increment the lowercase version's count
        elif word.lower() in self.words_to_counts:
            self.words_to_counts[word.lower()] += 1

        # if an uppercase version is in the dictionary, we know our input word must be lowercase.
        # since we only include uppercase words if they're always uppercase, we add the
        # lowercase version and give it the uppercase version's count
        elif word.capitalize() in self.words_to_counts:
            self.words_to_counts[word] = 1
            self.words_to_counts[word] += self.words_to_counts[word.capitalize()]
            del self.words_to_counts[word.capitalize()]

        # otherwise, the word is not in the dictionary at all, lowercase or uppercase
        # so we add it to the dictionary
        else:
            self.words_to_counts[word] = 1



if __name__ == "__main__":
    s = "Two cakes were bought by Bill. He payed two dollar's O'Reilly Auto Parts" \
        "Stratford-On-Avon"
    # s = "Come on you young sailor men listen to me, I'll sing you a song of the fish in the sea"
    # s = "alsdkfjlaskdjfalsdkjf"
    # s = ""
    # s = ","
    my_class = WorldCloudData(s)
    print(my_class.words_to_counts)