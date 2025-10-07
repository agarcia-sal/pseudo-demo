from typing import List


def vowels_count(input_str: str) -> int:
    candidate_vowels: str = "aeiouAEIOU"
    total_vowel_count: int = 0
    current_pos: int = 0

    while current_pos < len(input_str):
        current_char: str = input_str[current_pos]
        if (
            current_char == candidate_vowels[0]
            or current_char == candidate_vowels[1]
            or current_char == candidate_vowels[2]
            or current_char == candidate_vowels[3]
            or current_char == candidate_vowels[4]
            or current_char == candidate_vowels[5]
            or current_char == candidate_vowels[6]
            or current_char == candidate_vowels[7]
            or current_char == candidate_vowels[8]
            or current_char == candidate_vowels[9]
        ):
            total_vowel_count += 1
        current_pos += 1

    last_index: int = len(input_str) - 1
    if last_index >= 0:
        final_char: str = input_str[last_index]
        if final_char == 'y':
            total_vowel_count += 1
        else:
            if final_char == 'Y':
                total_vowel_count += 1

    return total_vowel_count