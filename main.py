def main():
    path = "books/frankenstein.txt"
    text = get_text(path)
    count = count_words(text)
    chars_dict = get_chars_dict(text)
    chars_list = convert_dict_to_list(chars_dict)
    chars_list.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {path} ---")
    print(f"{count} words found in the document")
    print()
    for item in chars_list:
        print(f"The {item['character']} character was found {item['num']} times")
    print("--- End report ---")  

def sort_on(dict):
    return dict["num"]

def get_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    characters = {}
    for char in text:
        c = char.lower()
        if c in characters:
            characters[c] += 1
        else:
            characters[c] = 1
    return characters

def convert_dict_to_list(dict):
    chars_list = []
    for char in dict:
        if char.isalpha():
            new_dict = {}
            new_dict["character"] = char 
            new_dict["num"] = dict[char]
            chars_list.append(new_dict)
    return chars_list        


main()        