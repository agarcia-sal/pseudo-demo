from typing import Dict

def encode(text: str) -> str:
    map: Dict[str, str] = {}
    for c in "aeiouAEIOU":
        map[c] = chr(ord(c) + 2)

    swapped = []
    for ch in text:
        upper = 'A' <= ch <= 'Z'
        lower = 'a' <= ch <= 'z'
        if upper:
            swapped.append(ch.lower())
        elif lower:
            swapped.append(ch.upper())
        else:
            swapped.append(ch)
    swapped_str = ''.join(swapped)

    output = []
    for elem in swapped_str:
        if elem in map:
            output.append(map[elem])
        else:
            output.append(elem)
    return ''.join(output)