from typing import List


def words_string(input_string: str) -> List[str]:
    if input_string == "":
        return []

    temp_chars: List[str] = []

    idx = 0
    while idx < len(input_string):
        current_char = input_string[idx]
        if current_char == ",":
            temp_chars.append(" ")
        else:
            temp_chars.append(current_char)
        idx += 1

    assembled_string = ""
    for symbol in temp_chars:
        assembled_string += symbol

    result_words = assembled_string.split(" ")
    return result_words