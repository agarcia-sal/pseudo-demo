from typing import List


def words_string(input_string: str) -> List[str]:
    if input_string == "":
        return []

    temp_chars: List[str] = []

    index_counter: int = 0
    while index_counter < len(input_string):
        current_char: str = input_string[index_counter]
        if current_char == ',':
            temp_chars.append(' ')
        else:
            temp_chars.append(current_char)
        index_counter += 1

    combined: str = "".join(temp_chars)

    return combined.split(" ")