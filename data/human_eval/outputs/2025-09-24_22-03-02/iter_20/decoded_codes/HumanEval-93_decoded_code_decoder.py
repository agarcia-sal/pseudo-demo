from typing import Dict, List

def encode(message: str) -> str:
    vowels: List[str] = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    vowels_replace: Dict[str, str] = {}
    for current_vowel in vowels:
        ascii_value = ord(current_vowel)
        replaced_char = chr(ascii_value + 2)
        vowels_replace[current_vowel] = replaced_char
    message = message.swapcase()
    result_characters: List[str] = []
    for current_char in message:
        if current_char in vowels:
            result_characters.append(vowels_replace[current_char])
        else:
            result_characters.append(current_char)
    result_string = ''.join(result_characters)
    return result_string