from typing import Literal

def encode(input: str) -> str:
    vowels: set[str] = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    symbols: str = ""
    for char in input:
        flipped: str = char.upper() if 'a' <= char <= 'z' else char.lower()
        ascii_code: int = ord(flipped)
        is_vowel: bool = flipped in vowels
        transformed: str = chr(ascii_code + 2) if is_vowel else flipped
        symbols += transformed
    return symbols