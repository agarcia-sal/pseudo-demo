from typing import Dict

def histogram(test_string: str) -> Dict[str, int]:
    frequency_dictionary: Dict[str, int] = {}
    list_of_letters = test_string.split(" ")
    maximum_count = 0

    for letter in list_of_letters:
        if letter == "":
            continue
        current_count = list_of_letters.count(letter)
        if current_count > maximum_count:
            maximum_count = current_count

    if maximum_count > 0:
        for letter in list_of_letters:
            if letter != "" and list_of_letters.count(letter) == maximum_count:
                frequency_dictionary[letter] = maximum_count

    return frequency_dictionary