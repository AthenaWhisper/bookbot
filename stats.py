def word_count(book):
    words = book.split()
    count = 0
    for word in words:
        count += 1
    return count

def letter_count(words):
    letter_dict = {}
    for letter in words:
        if letter.isalpha():
            to_lowercase = letter.lower()
            if to_lowercase not in letter_dict:
                letter_dict[to_lowercase[0]] = 1
            else:
                letter_dict[to_lowercase[0]] += 1
    return letter_dict

def sort_by(list):
    return list["num"]

def sort_dict(dictionary):
    sorted_list = []
    for char in dictionary:
        temp_dict = {"char": "", "num": 0}
        count = dictionary[char]
        temp_dict["char"] = char
        temp_dict["num"] = count
        sorted_list.append(temp_dict)
    sorted_list.sort(reverse=True, key=sort_by)
    return sorted_list