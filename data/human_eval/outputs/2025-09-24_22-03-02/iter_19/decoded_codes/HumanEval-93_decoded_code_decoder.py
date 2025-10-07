from typing import List, Dict

def encode(message: str) -> str:
    vowels: List[str] = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    vowels_replace: Dict[str, str] = {}
    index: int = 0
    while index < len(vowels):
        current_vowel = vowels[index]
        ascii_value = ord(current_vowel)
        new_char_ascii = ascii_value + 2
        new_char = chr(new_char_ascii)
        vowels_replace[current_vowel] = new_char
        index += 1
    message = message.swapcase()
    encoded_message: List[str] = []
    index = 0
    while index < len(message):
        current_char = message[index]
        if current_char in vowels:
            encoded_message.append(vowels_replace[current_char])
        else:
            encoded_message.append(current_char)
        index += 1
    return ''.join(encoded_message)