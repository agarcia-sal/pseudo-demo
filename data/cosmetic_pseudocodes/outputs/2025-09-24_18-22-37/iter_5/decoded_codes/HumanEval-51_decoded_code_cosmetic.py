from typing import List

def remove_vowels(input_string: str) -> str:
    vowel_chars: List[str] = ["a", "e", "i", "o", "u"]
    result_chars: List[str] = []
    index_counter: int = 0
    while index_counter < len(input_string):
        current_char: str = input_string[index_counter]
        lowercase_char: str = current_char.lower()
        if (lowercase_char == vowel_chars[0] or
            lowercase_char == vowel_chars[1] or
            lowercase_char == vowel_chars[2] or
            lowercase_char == vowel_chars[3] or
            lowercase_char == vowel_chars[4]):
            pass
        else:
            result_chars.append(current_char)
        index_counter += 1
    return "".join(result_chars)