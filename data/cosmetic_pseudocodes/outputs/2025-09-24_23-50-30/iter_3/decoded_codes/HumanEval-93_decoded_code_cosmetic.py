from typing import Dict

def encode(message: str) -> str:
    vowels_str: str = "aeiouAEIOU"
    transformed_map: Dict[str, str] = {}
    for ch in vowels_str:
        transformed_map[ch] = chr(ord(ch) + 2)

    toggled = []
    for ch in message:
        if ch.isupper():
            toggled.append(ch.lower())
        else:
            toggled.append(ch.upper())
    toggled_str = "".join(toggled)

    result = []
    for ch in toggled_str:
        if ch in transformed_map:
            result.append(transformed_map[ch])
        else:
            result.append(ch)
    return "".join(result)