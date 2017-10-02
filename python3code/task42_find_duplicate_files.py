# You left your computer unlocked and your friend decided to troll you by copying a lot of your files to random spots all over your file system.
# Even worse, she saved the duplicate files with random, embarrassing names ("this_is_like_a_digital_wedgie.txt" was clever, I'll give her that).
#
# Write a function that returns a list of all the duplicate files. We'll check them by hand before actually deleting them, since programmatically deleting files is really scary. To help us confirm that two files are actually duplicates, return a list of tuples ↴ where:
#
# the first item is the duplicate file
# the second item is the original file
# For example:
# [('/tmp/parker_is_dumb.mpg', '/home/parker/secret_puppy_dance.mpg'),
#  ('/home/trololol.mov', '/etc/apache2/httpd.conf')]
# You can assume each file was only duplicated once.

import os
import hashlib
from pprint import pprint
root_path = r"C:\Users\bkapusta\Documents\Personal Files\interviewcake"

def find_duplicates(starting_dircetory):
    files_seen_already = {}
    stack = [starting_dircetory]

    # we'll track tuples of (duplicate_file, original_file)
    duplicates = []
    while stack:
        current_path = stack.pop()
        # if current path is directory, put all files and folders in our stack
        if os.path.isdir(current_path):
            # os.listdir(current_path) will return list of contents in current directory
            for path in os.listdir(current_path):
                full_path = os.path.join(current_path, path)
                stack.append(full_path)
        # if it's a file:
        else:
            # we get file's hash
            file_hash = sample_hash_file(current_path)

            # get its last edited time
            current_last_edited_time = os.path.getmtime(current_path)

            # if we seen this file before (seen same hash)
            if file_hash in files_seen_already:
                existing_last_edited_time, existing_path = files_seen_already[file_hash]

                if current_last_edited_time > existing_last_edited_time:
                    # current file is the dupe!
                    duplicates.append((current_path, existing_path))

                else:
                    # old file is the dupe!
                    duplicates.append((existing_path, current_path))

                    # but also update files_seen_already to have the new file's info
                    files_seen_already[file_hash] = \
                        (current_last_edited_time, current_path)
            # if it's a new file, throw it in files_seen_already
            # and record its path and last edited time,
            # so we can tell later if it's a dupe
            else:
                files_seen_already[file_hash] = \
                (current_last_edited_time, current_path)

    return duplicates


def sample_hash_file(path):
    num_bytes_to_read_per_sample = 4000
    total_bytes = os.path.getsize(path)
    # we create hasher class, so
    hasher = hashlib.sha512()
    with open(path, 'rb') as file:

        # if the file is too short to take 3 samples, hash the entire file
        if total_bytes < num_bytes_to_read_per_sample * 3:
            hasher.update(file.read())

        else:
            num_bytes_between_samples = (total_bytes - num_bytes_to_read_per_sample * 3) // 2

            # read first, middle, and last bytes
            for offset_multiplier in range(3):
                start_of_sample = offset_multiplier * (num_bytes_to_read_per_sample + num_bytes_between_samples)
                file.seek(start_of_sample) # file.seek(5) # Go to the 6th byte in the file

                sample = file.read(num_bytes_to_read_per_sample)

                hasher.update(sample)

    return hasher.hexdigest()
pprint(find_duplicates(root_path))