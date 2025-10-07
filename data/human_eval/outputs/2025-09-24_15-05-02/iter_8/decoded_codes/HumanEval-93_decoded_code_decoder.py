from typing import Dict

def encode(message: str) -> str:
    vowels = "aeiouAEIOU"

    def shift_char(c: str) -> str:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            offset = (ord(c) - base + 2) % 26
            return chr(base + offset)
        return c

    vowels_replace: Dict[str, str] = {vowel: shift_char(vowel) for vowel in vowels}

    swapped_message = message.swapcase()
    result_chars = [vowels_replace[c] if c in vowels else c for c in swapped_message]

    return ''.join(result_chars)