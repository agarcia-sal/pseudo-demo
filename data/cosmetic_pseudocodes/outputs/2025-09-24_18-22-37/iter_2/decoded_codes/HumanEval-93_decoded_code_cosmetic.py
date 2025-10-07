from typing import Dict


def encode(inputText: str) -> str:
    vowelsStr: str = "aeiouAEIOU"
    substitutionMap: Dict[str, str] = {
        ch: chr(ord(ch) + 2) for ch in vowelsStr
    }

    toggledText = ''.join(
        c.lower() if c.isupper() else c.upper() if c.islower() else c
        for c in inputText
    )

    resultText = ''.join(
        substitutionMap.get(char, char)
        for char in toggledText
    )

    return resultText