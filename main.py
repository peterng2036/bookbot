from typing import Dict
from stats import get_book_text, count_words, get_num_of_char, sort_dict_with_count_desc
import sys

def print_report(file_path, words_count, charc_dict: Dict[str, int]):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")
    for charc in charc_dict.keys():
        print(f"{charc}: {charc_dict[charc]}")
    print("============= END ===============")
    
def get_file_path():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        return sys.argv[1]

def main():
    file_path = get_file_path()
    file_content = get_book_text(file_path)
    words_count = count_words(file_content)
    char_dict = get_num_of_char(file_content)
    sorted_dict = sort_dict_with_count_desc(char_dict)
    print_report(file_path, words_count, sorted_dict)
    

main()