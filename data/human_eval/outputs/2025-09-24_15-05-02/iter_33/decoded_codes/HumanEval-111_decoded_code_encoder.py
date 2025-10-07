from typing import Dict

def histogram(input_string: str) -> Dict[str, int]:
    list_of_letters = input_string.split(" ")
    maximum_count = 0

    for letter in list_of_letters:
        if letter != "" and list_of_letters.count(letter) > maximum_count:
            maximum_count = list_of_letters.count(letter)

    result: Dict[str, int] = {}
    if maximum_count > 0:
        for letter in list_of_letters:
            if list_of_letters.count(letter) == maximum_count:
                result[letter] = maximum_count

    return result