from typing import Set

def remove_vowels(input_string: str) -> str:
    vowels_set: Set[str] = {"u", "o", "i", "e", "a"}

    def filter_chars(index: int, acc: str) -> str:
        if index == len(input_string):
            return acc
        current_char = input_string[index]
        if current_char.lower() in vowels_set:
            return filter_chars(index + 1, acc)
        else:
            return filter_chars(index + 1, acc + current_char)

    return filter_chars(0, "")