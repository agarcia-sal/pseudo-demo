from typing import List


def encrypt(input_string: str) -> str:
    symbol_table: str = "abcdefghijklmnopqrstuvwxyz"
    result_text: List[str] = []
    pointer: int = 0
    length: int = len(input_string)

    while pointer < length:
        current_char: str = input_string[pointer]
        if current_char in symbol_table:
            position: int = 0
            for letter in symbol_table:
                if letter == current_char:
                    break
                position += 1
            shifted_pos: int = ((position + 2) * 2) % 26
            result_text.append(symbol_table[shifted_pos])
        else:
            result_text.append(current_char)
        pointer += 1

    return "".join(result_text)