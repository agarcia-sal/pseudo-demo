from typing import Dict

def encode(text: str) -> str:
    vowels_set = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

    vowel_map: Dict[str, str] = {letter: chr(ord(letter) + 2) for letter in vowels_set}

    transformed = []
    for ch in text:
        swapped = ch.lower() if ch.isupper() else ch.upper()
        transformed.append(swapped)

    result = []
    for sym in transformed:
        if sym in vowels_set:
            result.append(vowel_map[sym])
        else:
            result.append(sym)

    return ''.join(result)