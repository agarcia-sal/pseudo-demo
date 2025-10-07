from typing import Dict, Set


def encode(text: str) -> str:
    target_vowels: Set[str] = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    shift_map: Dict[str, str] = {symbol: chr(ord(symbol) + 2) for symbol in target_vowels}

    def swap_case(s: str) -> str:
        idx: int = 0
        swapped_chars: list[str] = []
        while idx < len(s):
            ch = s[idx]
            # If character is uppercase, convert to lowercase, else uppercase
            if ch == ch.upper():
                swapped_chars.append(ch.lower())
            else:
                swapped_chars.append(ch.upper())
            idx += 1
        return "".join(swapped_chars)

    transformed_text = swap_case(text)

    output_chars: list[str] = []
    i: int = 0
    while i < len(transformed_text):
        c = transformed_text[i]
        if c in target_vowels:
            output_chars.append(shift_map[c])
        else:
            output_chars.append(c)
        i += 1

    return "".join(output_chars)