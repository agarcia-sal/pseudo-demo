from typing import Dict

def encode(message: str) -> str:
    vowels: str = "AEIOUaeiou"
    # Map each vowel to the character two Unicode code points ahead
    shifted_vowels: Dict[str, str] = {ch: chr(ord(ch) + 2) for ch in vowels}

    transformed: str = ""
    remaining: str = message

    while remaining:
        head: str = remaining[0]
        tail: str = remaining[1:]
        if head in vowels:
            replacement: str = shifted_vowels[head]
        else:
            replacement = head
        transformed += replacement
        remaining = tail

    result: str = ""
    for ch in transformed:
        if ch.isalpha():
            result += ch.upper() if ch.islower() else ch.lower()
        else:
            result += ch

    return result