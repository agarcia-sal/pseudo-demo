from typing import Dict

def encode(message: str) -> str:
    vowels_collection: str = "aeiouAEIOU"

    def shiftChar(c: str) -> str:
        return chr(ord(c) + 2)

    vowel_replacements: Dict[str, str] = {vowel_char: shiftChar(vowel_char) for vowel_char in vowels_collection}

    toggled_message_chars = [
        ch.upper() if ch.islower() else ch.lower() if ch.isupper() else ch
        for ch in message
    ]
    toggled_message: str = "".join(toggled_message_chars)

    output_chars = [
        vowel_replacements[letter] if letter in vowel_replacements else letter
        for letter in toggled_message
    ]

    return "".join(output_chars)