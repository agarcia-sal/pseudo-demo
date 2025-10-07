from typing import Dict

def histogram(test_string: str) -> Dict[str, int]:
    frequency_dict: Dict[str, int] = {}
    list_of_letters = test_string.split(' ')
    max_count = 0

    # Compute max_count by checking counts of non-empty letters
    for letter in list_of_letters:
        if letter and list_of_letters.count(letter) > max_count:
            max_count = list_of_letters.count(letter)

    if max_count > 0:
        for letter in list_of_letters:
            if list_of_letters.count(letter) == max_count:
                frequency_dict[letter] = max_count

    return frequency_dict