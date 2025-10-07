from typing import List


def remove_vowels(input_string: str) -> str:
    output_chars: List[str] = []
    index_counter: int = 0

    while index_counter < len(input_string):
        current_char: str = input_string[index_counter]
        char_lowercase: str = current_char.lower()

        if char_lowercase in {"a", "e", "i", "o", "u"}:
            pass  # skip vowels
        else:
            output_chars.append(current_char)

        index_counter += 1

    return "".join(output_chars)