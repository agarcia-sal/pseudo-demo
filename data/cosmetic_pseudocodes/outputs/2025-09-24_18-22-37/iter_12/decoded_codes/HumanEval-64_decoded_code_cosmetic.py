from typing import Sequence

def vowels_count(alphabet_sequence: Sequence[str]) -> int:
    allowed_chars = "aeiouAEIOU"
    count_accumulator = 0
    position_tracker = 0
    length = len(alphabet_sequence)

    while position_tracker < length:
        current_symbol = alphabet_sequence[position_tracker]
        if current_symbol in allowed_chars:
            count_accumulator += 1
        position_tracker += 1

    last_index = length - 1
    if last_index >= 0:
        final_char = alphabet_sequence[last_index]
        if final_char == 'y' or final_char == 'Y':
            count_accumulator += 1

    return count_accumulator