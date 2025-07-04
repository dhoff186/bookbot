from stats import char_count
from stats import dict_sorted
from stats import number_of_words
import sys


def get_book_txt(input_path):
    with open(input_path) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    print("============ BOOKBOT ==========")
    print("Analyzing book...")
    print("----------- Word Count ----------")
    all_txt = get_book_txt(book_path)
    number_of_words(all_txt)

    number_of_characters = char_count(all_txt)
    sorted_chars = dict_sorted(number_of_characters)
    print("--------- Character Count -------")
    for i in sorted_chars:
        if i["char"].isalpha():
            print(f"{i['char']}: {i['num']}")

    print("============= END ===============")


main()
