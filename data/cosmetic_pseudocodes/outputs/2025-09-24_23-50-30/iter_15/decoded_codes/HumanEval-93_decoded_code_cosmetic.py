from typing import Dict

def encode(original: str) -> str:
    vowel_set = ['a','e','i','o','u','A','E','I','O','U']

    shift_map: Dict[str, str] = {}
    for c in vowel_set:
        shifted_char = chr(ord(c) + 2)
        shift_map[c] = shifted_char

    swapped = []
    for each_char in original:
        if each_char.islower():
            swapped_char = each_char.upper()
        elif each_char.isupper():
            swapped_char = each_char.lower()
        else:
            swapped_char = each_char
        swapped.append(swapped_char)

    result = []
    for char in swapped:
        if char in shift_map:
            result.append(shift_map[char])
        else:
            result.append(char)

    return ''.join(result)