from typing import Dict


def encode(message: str) -> str:
    vowels: str = "aeiouAEIOU"
    vowels_replace: Dict[str, str] = {
        v: chr(ord(v) + 2) for v in vowels
    }
    swapped_message: str = message.swapcase()
    # Replace letters in swapped_message if they are vowels in the original vowels set
    return "".join(vowels_replace.get(ch, ch) for ch in swapped_message)