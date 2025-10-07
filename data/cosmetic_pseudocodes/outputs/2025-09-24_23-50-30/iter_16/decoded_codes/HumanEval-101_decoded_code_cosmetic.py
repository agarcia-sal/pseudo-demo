from typing import List


def words_string(input_string: str) -> List[str]:
    if input_string == "":
        return []

    chars_map: List[str] = []
    idx_counter: int = 0

    while idx_counter < len(input_string):
        if input_string[idx_counter] == ",":
            chars_map.append(" ")
        else:
            chars_map.append(input_string[idx_counter])
        idx_counter += 1

    merged_string: str = ""
    idx_iter: int = 0

    while idx_iter < len(chars_map):
        merged_string += chars_map[idx_iter]
        idx_iter += 1

    return merged_string.split()