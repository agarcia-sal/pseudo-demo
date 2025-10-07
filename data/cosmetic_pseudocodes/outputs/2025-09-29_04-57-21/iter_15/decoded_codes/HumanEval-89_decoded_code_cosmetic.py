from typing import Union


def encrypt(input_string: str) -> str:
    letters = "abcdefghijklmnopqrstuvwxyz"
    result = []
    position = 0
    length = len(input_string)

    while position < length:
        current_char = input_string[position]
        if current_char in letters:
            current_pos = 0
            while current_pos < len(letters):
                if letters[current_pos] == current_char:
                    break
                current_pos += 1
            val = (current_pos + 2) * 2
            new_index = val - 26 * (val // 26)
            result.append(letters[new_index])
        else:
            result.append(current_char)
        position += 1

    return "".join(result)