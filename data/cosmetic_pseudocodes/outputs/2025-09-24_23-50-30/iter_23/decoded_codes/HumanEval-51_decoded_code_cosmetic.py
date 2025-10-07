from typing import List

def remove_vowels(input_string: str) -> str:
    filtered_chars: List[str] = [
        letter for letter in input_string if letter.lower() not in {'a', 'e', 'i', 'o', 'u'}
    ]
    return ''.join(filtered_chars)