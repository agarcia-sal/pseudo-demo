from typing import List

def remove_vowels(input_string: str) -> str:
    letters_retained: List[str] = []
    for char_element in input_string:
        vowel_check = char_element.lower()
        if vowel_check not in {"a", "e", "i", "o", "u"}:
            letters_retained.append(char_element)
    combined_string = "".join(letters_retained)
    return combined_string