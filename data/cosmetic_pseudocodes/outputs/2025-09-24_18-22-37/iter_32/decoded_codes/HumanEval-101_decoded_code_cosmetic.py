from typing import List

def words_string(input_string: str) -> List[str]:
    if not input_string:
        return []

    buffer_list: List[str] = []

    idx_counter: int = 0
    while idx_counter < len(input_string):
        current_char: str = input_string[idx_counter]

        if current_char != ',':
            buffer_list.append(current_char)
        else:
            buffer_list.append(' ')

        idx_counter += 1

    temp_string: str = ""
    pos: int = 0

    while pos < len(buffer_list):
        temp_string += buffer_list[pos]
        pos += 1

    return temp_string.split()