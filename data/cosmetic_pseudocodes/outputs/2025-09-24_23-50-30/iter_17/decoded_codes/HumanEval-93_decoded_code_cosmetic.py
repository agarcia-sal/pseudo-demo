from typing import Dict, List


def encode(input: str) -> str:
    vowels_set: str = "AEIOUaeiou"
    shifts: Dict[str, str] = {}

    for current in vowels_set:
        shifts[current] = chr(ord(current) + 2)

    swapped_chars: List[str] = []
    for ch in input:
        if 'a' <= ch <= 'z':
            swapped_chars.append(chr(ord(ch) - 32))
        elif 'A' <= ch <= 'Z':
            swapped_chars.append(chr(ord(ch) + 32))
        else:
            swapped_chars.append(ch)

    transformed = ''.join(shifts.get(symbol, symbol) for symbol in swapped_chars)
    return transformed