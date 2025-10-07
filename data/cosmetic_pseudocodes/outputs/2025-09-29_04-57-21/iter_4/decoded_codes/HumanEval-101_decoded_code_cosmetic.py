from typing import List


def words_string(input_string: str) -> List[str]:
    if not (input_string != ""):
        return []

    processed_chars: List[str] = []
    index_counter: int = 0

    while index_counter < len(input_string):
        current_char: str = input_string[index_counter]

        if current_char == ',':
            processed_chars.insert(len(processed_chars), ' ')
        else:
            processed_chars.insert(len(processed_chars), current_char)

        index_counter += 1

    accumulated_string: str = ""
    read_pos: int = 0

    while read_pos < len(processed_chars):
        accumulated_string += processed_chars[read_pos]
        read_pos += 1

    return accumulated_string.split()