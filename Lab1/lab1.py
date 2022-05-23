import math
import os
from typing import Counter


# problem 1 calculate distance
def calculate_destance(x_1, y_1, x_2, y_2):
    double_distance = pow((x_2-x_1), 2)+pow((y_2-y_1), 2)
    return math.sqrt(double_distance)


# problem 2 return list of uniques
test_list = [1, 2, 2, 3, 2]


def find_the_uniques(lst):
    print(list(set(lst)))

# return duplicates


def trsverse_list(lst):
    unique = set()
    dup = []
    for num in lst:
        if num in unique:
            dup.append(num)
        else:
            unique.add(num)
    print(unique)
    print(dup)


# find_the_uniques(test_list)

# problem 3 string formatting
word = 'abcde'
word2 = 'efghk'


def string_formatter(str_1, str_2):
    fst_str_slice_pos = find_slice_pos(str_1)
    sec_str_slice_pos = find_slice_pos(str_2)

    str_1_front = str_1[:fst_str_slice_pos]
    str_1_back = str_1[fst_str_slice_pos:]

    str_2_front = str_2[:sec_str_slice_pos]
    str_2_back = str_2[sec_str_slice_pos:]

    print(f"{str_1_front}-{str_2_front}-{str_1_back}-{str_2_back}.")


def find_slice_pos(test_str):
    return int(len(test_str)/2 if (len(test_str) % 2 == 0) else len(test_str)/2+1)

# string_formatter(word,word2)

# problem 4 reading file & extract most frequent words


def handle_file():
    # file_path = input('enter file path :')
    file_path = './testSample.txt'
    if os.path.isfile(file_path):
        file = open(file_path, 'rt', encoding='utf8')
        file_list = file.read().split()
        # frequent_words = Counter(file_list).most_common(20)  # will return key value pair of the (words,counter)
        frequent_words = [key for key, val in Counter(
            file_list).most_common(20)]
        print(frequent_words)
        # write most frequent to new txt file
        freq_file = open('popular_words.txt', 'w', encoding='utf8')
        freq_file.write('-'.join(frequent_words))
    else:
        print('FILE NOT FOUND')


# handle_file()

# problem 5 finding vowls
vowls = {'u': 0, 'o': 0, 'e': 0, 'a': 0, 'i': 0}


def finding_vowls(test_word):
    non_vowls_chars = ''
    for letter in test_word:
        letter = letter.casefold()
        if letter in vowls:
            vowls[letter] += 1
        else:
            non_vowls_chars += letter
    print(non_vowls_chars)
    print(vowls)


finding_vowls('Mobile')
finding_vowls('MobIle')

#problem 6 find occurence of letter 
def find_letter_in_word(test_word,letter):
    return [index for index, ch in enumerate(test_word) if ch == letter]


print(find_letter_in_word('google','o'))
