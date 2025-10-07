from typing import List


def remove_vowels(input_string: str) -> str:
    output_sequence: List[str] = []
    index: int = 0

    while index < len(input_string):
        current_char: str = input_string[index]
        if current_char.lower() not in {'a', 'e', 'i', 'o', 'u'}:
            output_sequence.append(current_char)
        index += 1

    result_string: str = ""
    for element in output_sequence:
        result_string += element

    return result_string