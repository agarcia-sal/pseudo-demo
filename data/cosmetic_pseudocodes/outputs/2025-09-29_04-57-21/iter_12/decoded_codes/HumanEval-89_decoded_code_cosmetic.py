from typing import List


def encrypt(input_string: str) -> str:
    alpha_seq: str = 'abcdefghijklmnopqrstuvwxyz'
    result_str: str = ''
    position: int = 0
    length: int = len(input_string)

    while position < length:
        curr_char: str = input_string[position]
        if curr_char not in alpha_seq:
            result_str += curr_char
            position += 1
            continue

        base_idx: int = 0
        while alpha_seq[base_idx] != curr_char:
            base_idx += 1

        new_idx: int = (base_idx + 4) % 26  # 2 * 2 = 4 shift
        result_str += alpha_seq[new_idx]
        position += 1

    return result_str