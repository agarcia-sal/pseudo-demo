from typing import List


def remove_vowels(input_str: str) -> str:
    result_chars: List[str] = []
    index_counter: int = 0

    while index_counter < len(input_str):
        current_char: str = input_str[index_counter]
        lower_char = current_char.lower()
        if not (lower_char == "a" or lower_char == "e" or lower_char == "i" or lower_char == "o" or lower_char == "u"):
            result_chars.append(current_char)
        index_counter += 1

    output_str: str = ""
    pos: int = 0

    while pos < len(result_chars):
        output_str += result_chars[pos]
        pos += 1

    return output_str