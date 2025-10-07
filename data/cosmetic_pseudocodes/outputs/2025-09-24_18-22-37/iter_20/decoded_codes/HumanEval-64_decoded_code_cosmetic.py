from typing import Sequence

def vowels_count(alpha_sequence: Sequence[str]) -> int:
    allowed_vowels = "aeiouAEIOU"
    current_position: int = 0
    total_vowels_identified: int = 0
    sequence_length: int = len(alpha_sequence)

    while current_position < sequence_length:
        present_char = alpha_sequence[current_position]
        is_present_char_vowel = False

        vowel_index = 0
        while vowel_index < len(allowed_vowels):
            vowel_candidate = allowed_vowels[vowel_index]
            if present_char == vowel_candidate:
                is_present_char_vowel = True
                break
            vowel_index += 1

        if is_present_char_vowel:
            total_vowels_identified += 1

        current_position += 1

    if sequence_length == 0:
        return total_vowels_identified

    terminal_char = alpha_sequence[sequence_length - 1]
    if terminal_char == 'y' or terminal_char == 'Y':
        total_vowels_identified += 1

    return total_vowels_identified