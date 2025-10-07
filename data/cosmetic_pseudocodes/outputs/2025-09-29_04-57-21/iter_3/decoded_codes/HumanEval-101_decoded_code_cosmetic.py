from typing import List


def words_string(input_string: str) -> List[str]:
    if not input_string:
        return []

    temp_chars: List[str] = []
    for idx in range(len(input_string)):
        current_char = input_string[idx]
        if current_char == ",":
            temp_chars.append(" ")
        else:
            temp_chars.append(current_char)

    combined_string = "".join(temp_chars)
    return combined_string.split()