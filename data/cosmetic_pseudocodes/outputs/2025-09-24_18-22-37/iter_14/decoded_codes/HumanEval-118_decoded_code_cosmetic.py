from typing import Set


def get_closest_vowel(letter_sequence: str) -> str:
    result_string: str = ""
    sequence_length: int = len(letter_sequence)
    if sequence_length < 3:
        return result_string

    vowel_collection: Set[str] = {"a", "A", "e", "E", "i", "I", "o", "O", "u", "U"}
    position_iterator: int = 1

    while position_iterator <= (sequence_length - 2):
        current_index: int = (sequence_length - 1) - (position_iterator - 1)
        current_char: str = letter_sequence[current_index]

        if current_char in vowel_collection:
            next_char: str = letter_sequence[current_index + 1]
            previous_char: str = letter_sequence[current_index - 1]

            is_next_vowel: bool = next_char in vowel_collection
            is_previous_vowel: bool = previous_char in vowel_collection

            if not is_next_vowel and not is_previous_vowel:
                result_string = current_char
                return result_string

        position_iterator += 1

    return result_string