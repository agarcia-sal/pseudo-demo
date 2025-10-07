from typing import Dict

def histogram(test_string: str) -> Dict[str, int]:
    frequency_dictionary: Dict[str, int] = {}
    list_of_letters = test_string.split(" ")
    maximum_count = 0

    for letter_candidate in list_of_letters:
        if letter_candidate == "":
            continue
        letter_freq = list_of_letters.count(letter_candidate)
        if letter_freq > maximum_count:
            maximum_count = letter_freq

    if maximum_count <= 0:
        return frequency_dictionary

    for current_letter in list_of_letters:
        current_count = list_of_letters.count(current_letter)
        if current_count == maximum_count:
            frequency_dictionary[current_letter] = maximum_count

    return frequency_dictionary