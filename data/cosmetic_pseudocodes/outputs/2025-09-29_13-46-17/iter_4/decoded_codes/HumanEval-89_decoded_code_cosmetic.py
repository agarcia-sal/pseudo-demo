from typing import List


def encrypt(input_string: str) -> str:
    ALPHABET: str = 'abcdefghijklmnopqrstuvwxyz'
    result_accumulator: List[str] = []

    def process_characters(position: int) -> None:
        if position >= len(input_string):
            return
        current_char = input_string[position]
        index = ALPHABET.find(current_char)
        if index != -1:
            transformed_pos = (index + 4) % 26  # 2*2 = 4
            result_accumulator.append(ALPHABET[transformed_pos])
        else:
            result_accumulator.append(current_char)
        process_characters(position + 1)

    process_characters(0)
    return ''.join(result_accumulator)