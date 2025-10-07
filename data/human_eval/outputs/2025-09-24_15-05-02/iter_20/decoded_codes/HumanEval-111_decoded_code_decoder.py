from typing import Dict

def histogram(test: str) -> Dict[str, int]:
    dict1: Dict[str, int] = {}
    list1 = test.split(" ")
    max_count = 0

    # Determine the maximum frequency of any non-empty word
    for letter in list1:
        if letter and list1.count(letter) > max_count:
            max_count = list1.count(letter)
    if max_count > 0:
        for letter in list1:
            if list1.count(letter) == max_count:
                dict1[letter] = max_count
    return dict1