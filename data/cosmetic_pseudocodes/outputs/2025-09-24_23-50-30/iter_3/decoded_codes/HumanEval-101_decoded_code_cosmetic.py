from typing import List

def words_string(input_string: str) -> List[str]:
    if input_string == "":
        return []

    chars_accum: List[str] = []
    index = 0  # zero-based index for Python strings

    while index < len(input_string):
        current_char = input_string[index]
        if current_char == ",":
            chars_accum.append(" ")
        else:
            chars_accum.append(current_char)
        index += 1

    merged = "".join(chars_accum)
    return merged.split()