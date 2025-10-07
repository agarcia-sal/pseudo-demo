from typing import List

def remove_vowels(text: str) -> str:
    filtered_chars: List[str] = []
    index: int = 0
    while index < len(text):
        current_char: str = text[index]
        if current_char.lower() not in {'a', 'e', 'i', 'o', 'u'}:
            filtered_chars.append(current_char)
        index += 1
    result: str = ''
    for char_element in filtered_chars:
        result += char_element
    return result