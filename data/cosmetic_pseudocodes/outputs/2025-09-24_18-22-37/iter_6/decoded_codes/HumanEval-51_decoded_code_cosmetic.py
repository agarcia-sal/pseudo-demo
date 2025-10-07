from typing import List


def remove_vowels(input_string: str) -> str:
    filtered_chars: List[str] = []
    index_counter: int = 0
    vowels = {'a', 'e', 'i', 'o', 'u'}
    while index_counter < len(input_string):
        current_char = input_string[index_counter]
        lower_char = current_char.lower()
        vowel_check = lower_char in vowels
        if not vowel_check:
            filtered_chars.append(current_char)
        index_counter += 1
    result_string = ''
    cursor = 0
    while cursor < len(filtered_chars):
        result_string += filtered_chars[cursor]
        cursor += 1
    return result_string