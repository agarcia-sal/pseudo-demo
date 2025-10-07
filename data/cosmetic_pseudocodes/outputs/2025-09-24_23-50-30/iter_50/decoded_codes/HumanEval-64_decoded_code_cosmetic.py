from typing import Sequence

def vowels_count(input_sequence: Sequence[str]) -> int:
    vowel_collection = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    total_vowels_found: int = 0
    current_index: int = 0
    seq_length: int = len(input_sequence)

    while current_index < seq_length:
        current_char: str = input_sequence[current_index]
        is_vowel_char: bool = False
        for candidate in vowel_collection:
            if candidate == current_char:
                is_vowel_char = True
        total_vowels_found += 1 if is_vowel_char else 0
        current_index += 1

    final_character: str = input_sequence[seq_length - 1] if seq_length > 0 else '\0'
    if final_character in ('y', 'Y'):
        total_vowels_found += 1

    return total_vowels_found