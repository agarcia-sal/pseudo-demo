from typing import List

def remove_vowels(input_string: str) -> str:
    vowels_map = {"a": 1, "e": 1, "i": 1, "o": 1, "u": 1}
    result_chars: List[str] = []

    def filter_at(index: int) -> None:
        if index == len(input_string):
            return
        current_char = input_string[index]
        lower_char = current_char.lower()
        if lower_char not in vowels_map:
            result_chars.append(current_char)
        filter_at(index + 1)

    filter_at(0)
    return "".join(result_chars)