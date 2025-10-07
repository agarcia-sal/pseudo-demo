from typing import List


def encrypt(input_string: str) -> str:
    chars_sequence: str = 'abcdefghijklmnopqrstuvwxyz'
    result_accumulator: str = ''
    processed_chars: List[str] = list(input_string)

    for position in range(len(processed_chars)):
        current_char: str = processed_chars[position]
        if current_char in chars_sequence:
            index_tracker: int = (chars_sequence.index(current_char) + (2 * 2)) % 26
            result_accumulator += chars_sequence[index_tracker]
        else:
            result_accumulator += current_char

    return result_accumulator