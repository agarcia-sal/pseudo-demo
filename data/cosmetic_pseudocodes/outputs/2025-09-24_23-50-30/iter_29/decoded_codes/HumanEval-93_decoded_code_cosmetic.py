from typing import Dict

def encode(text: str) -> str:
    vowelset = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    mapdict: Dict[str, str] = {char: chr(ord(char) + 2) for char in vowelset}

    swapped = []
    for idx in range(len(text) - 1):
        c = text[idx]
        if 'a' <= c <= 'z':
            swapped.append(chr(ord(c) - 32))  # to uppercase
        elif 'A' <= c <= 'Z':
            swapped.append(chr(ord(c) + 32))  # to lowercase
        else:
            swapped.append(c)
    swapped_str = "".join(swapped)

    result = []
    for ch in swapped_str:
        result.append(mapdict[ch] if ch in vowelset else ch)

    return "".join(result)