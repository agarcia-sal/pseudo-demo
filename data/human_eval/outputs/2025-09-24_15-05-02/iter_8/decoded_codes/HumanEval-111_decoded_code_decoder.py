from typing import Dict

def histogram(test_string: str) -> Dict[str, int]:
    list_of_letters = test_string.split(" ")
    count_dict: Dict[str, int] = {}
    max_count = 0

    for letter in list_of_letters:
        if letter:
            count_dict[letter] = count_dict.get(letter, 0) + 1
            if count_dict[letter] > max_count:
                max_count = count_dict[letter]

    if max_count > 0:
        return {letter: max_count for letter, count in count_dict.items() if count == max_count}
    return {}