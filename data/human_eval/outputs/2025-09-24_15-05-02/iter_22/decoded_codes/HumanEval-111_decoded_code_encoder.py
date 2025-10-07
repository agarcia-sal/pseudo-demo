from typing import Dict

def histogram(input_string: str) -> Dict[str, int]:
    frequency_dictionary: Dict[str, int] = {}
    list_of_letters = input_string.split(' ')
    maximum_count: int = 0

    # Determine maximum count among non-empty letters
    for letter in list_of_letters:
        if letter != "":
            count = list_of_letters.count(letter)
            if count > maximum_count:
                maximum_count = count

    # Collect letters that have the maximum count
    if maximum_count > 0:
        seen_letters = set()
        for letter in list_of_letters:
            if letter != "" and list_of_letters.count(letter) == maximum_count and letter not in seen_letters:
                frequency_dictionary[letter] = maximum_count
                seen_letters.add(letter)

    return frequency_dictionary