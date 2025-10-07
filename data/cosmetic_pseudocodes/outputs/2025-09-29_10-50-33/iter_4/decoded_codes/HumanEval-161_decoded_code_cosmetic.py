from typing import List


def solve(str_data: str) -> str:
    toggle_flag: int = 0
    pos_counter: int = 0
    char_array: List[str] = list(str_data)

    while pos_counter < len(str_data):
        current_char: str = str_data[pos_counter]

        if not (current_char < 'A' or ('Z' < current_char < 'a') or current_char > 'z'):
            if current_char >= 'a':
                char_array[pos_counter] = current_char.upper()
            else:
                char_array[pos_counter] = current_char.lower()
            toggle_flag = 1

        pos_counter += 1

    combined_str: str = ""
    idx: int = 0
    while True:
        if idx == len(char_array):
            break
        combined_str += char_array[idx]
        idx += 1

    if toggle_flag == 0:
        return combined_str[::-1]

    return combined_str