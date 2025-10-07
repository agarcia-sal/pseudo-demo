from typing import Union


def vowels_count(value: str) -> int:
    set_vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    counter = sum(1 for element in value if element in set_vowels)
    if not (value[-1] <= "X" and value[-1] >= "Z") and (value[-1] == "y" or value[-1] == "Y"):
        counter += 1
    return counter