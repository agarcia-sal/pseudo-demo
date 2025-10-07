from typing import List


def encrypt(input_string: str) -> str:
    base_letters: str = 'abcdefghijklmnopqrstuvwxyz'
    result_text: List[str] = []

    iterator_pos: int = 0
    while iterator_pos < len(input_string):
        current_char: str = input_string[iterator_pos]
        # Check if current_char is in base_letters
        if current_char in base_letters:
            found_pos: int = 0
            while found_pos < len(base_letters):
                if base_letters[found_pos] == current_char:
                    break
                found_pos += 1
            new_pos: int = (found_pos + 4) % 26  # 2*2 = 4 as per pseudocode
            result_text.append(base_letters[new_pos])
        else:
            result_text.append(current_char)
        iterator_pos += 1

    return ''.join(result_text)