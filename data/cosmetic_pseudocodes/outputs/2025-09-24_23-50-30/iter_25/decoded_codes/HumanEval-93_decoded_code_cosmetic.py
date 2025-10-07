from typing import Dict


def encode(text: str) -> str:
    vowels_str: str = "aeiouAEIOU"
    shift_map: Dict[str, str] = {}

    # Build shift_map by shifting each vowel character by 2 positions in ASCII
    for position in range(len(vowels_str)):
        char = vowels_str[position]
        shift_map[char] = chr(ord(char) + 2)

    def swap_case(s: str) -> str:
        result = []
        for curr in s:
            if 'a' <= curr <= 'z':
                result.append(curr.upper())
            elif 'A' <= curr <= 'Z':
                result.append(curr.lower())
            else:
                result.append(curr)
        return ''.join(result)

    text = swap_case(text)

    transformed = []
    i = 0
    while i < len(text):
        ch = text[i]
        if ch in vowels_str:
            transformed.append(shift_map[ch])
        else:
            transformed.append(ch)
        i += 1

    return ''.join(transformed)