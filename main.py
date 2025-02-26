import sys

from stats import (
    count_words,
    get_chars_dict,
    convert_dict_to_list,
    sort_on
)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_text(path)
    count = count_words(text)
    chars_dict = get_chars_dict(text)
    chars_list = convert_dict_to_list(chars_dict)
    chars_list.sort(reverse=True, key=sort_on)
    report(path, count, chars_list)

def report(path, count, chars_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for item in chars_list:
        print(f"{item['character']}: {item['num']}")
    print("============= END ===============")  

def get_text(path):
    with open(path) as f:
        return f.read()

main()        
