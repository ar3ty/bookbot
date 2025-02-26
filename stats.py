def count_words(text):
    words = text.split()
    return len(words)

def sort_on(dict):
    return dict["num"]

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