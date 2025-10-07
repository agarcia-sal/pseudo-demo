from typing import Dict

def encode(input_text: str) -> str:
    vowel_characters: str = "AEIOUaeiou"
    map_char_replacement: Dict[str, str] = {
        char: chr(ord(char) + 2) for char in vowel_characters
    }
    flipped_text = ''.join(
        c.lower() if c.isupper() else c.upper()
        for c in input_text
    )
    result_chars = [
        map_char_replacement.get(character, character)
        for character in flipped_text
    ]
    return ''.join(result_chars)