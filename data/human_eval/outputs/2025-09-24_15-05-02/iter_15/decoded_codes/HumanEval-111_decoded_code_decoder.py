from typing import Dict

def histogram(test_string: str) -> Dict[str, int]:
    frequency_dictionary = {}
    list_of_letters = test_string.split(" ")
    max_count = 0

    for letter in list_of_letters:
        if letter != '' and list_of_letters.count(letter) > max_count:
            max_count = list_of_letters.count(letter)

    if max_count > 0:
        for letter in list_of_letters:
            if list_of_letters.count(letter) == max_count:
                frequency_dictionary[letter] = max_count

    return frequency_dictionary