from typing import Dict

def encode(text: str) -> str:
    vowelSet: list[str] = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    substitutionMap: Dict[str, str] = {item: chr(ord(item) + 2) for item in vowelSet}

    swappedText_chars = []
    for eachChar in text:
        ascii_val = ord(eachChar)
        if 'a' <= eachChar <= 'z':
            swappedText_chars.append(chr(ord('z') - (ascii_val - ord('a'))))
        elif 'A' <= eachChar <= 'Z':
            swappedText_chars.append(chr(ord('Z') - (ascii_val - ord('A'))))
        else:
            swappedText_chars.append(eachChar)
    swappedText = ''.join(swappedText_chars)

    output_chars = [
        substitutionMap[eachElement] if eachElement in substitutionMap else eachElement
        for eachElement in swappedText
    ]

    return ''.join(output_chars)