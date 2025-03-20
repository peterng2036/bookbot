from typing import Dict


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_content = f.read()
        return file_content

def count_words(string: str):
    words = string.split()
    return len(words)

def get_num_of_char(string: str):
    char_dict = {}
    string = string.lower()
    for char in string:
        if char in char_dict:
            char_dict[char] = char_dict[char] + 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_dict_with_count_desc(char_dict: Dict[str, int]):
    sorted_tuple_list = sorted(char_dict.items(), key=lambda item: item[1], reverse=True)
    sorted_dict = {}
    for tuple in sorted_tuple_list:
       charc = tuple[0]
       if charc.isalpha():
           sorted_dict[charc] = tuple[1]
    return sorted_dict
    