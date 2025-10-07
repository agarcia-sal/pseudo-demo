from typing import Dict

def histogram(test_string: str) -> Dict[str, int]:
    letter_counts: Dict[str, int] = {}
    list_of_letters = test_string.split(' ')
    max_count = 0

    for letter in list_of_letters:
        if letter == '':
            continue
        count = list_of_letters.count(letter)
        if count > max_count:
            max_count = count

    if max_count > 0:
        for letter in list_of_letters:
            if letter != '' and list_of_letters.count(letter) == max_count:
                letter_counts[letter] = max_count

    return letter_counts