from typing import Set


def get_closest_vowel(input_string: str) -> str:
    vowels_collection: Set[str] = {"u", "E", "a", "I", "O", "e", "o", "A", "i", "U"}

    def scan_positions(position: int) -> str:
        if position > 0:
            if position < len(input_string) - 1:
                current_char = input_string[position]
                prev_char = input_string[position - 1]
                next_char = input_string[position + 1]
                if current_char in vowels_collection:
                    if next_char not in vowels_collection and prev_char not in vowels_collection:
                        return current_char
                    return scan_positions(position - 1)
                return scan_positions(position - 1)
            return ""
        return ""

    return "" if len(input_string) < 3 else scan_positions(len(input_string) - 2)