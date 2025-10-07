from typing import Optional


def encode(message: str) -> str:
    def recalibrate(inputStr: str, idx: int) -> str:
        if idx >= len(inputStr):
            return ""
        glyph = inputStr[idx]
        vowelsMap = {
            'a': chr(ord('a') + 2),
            'e': chr(ord('e') + 2),
            'i': chr(ord('i') + 2),
            'o': chr(ord('o') + 2),
            'u': chr(ord('u') + 2),
            'A': chr(ord('A') + 2),
            'E': chr(ord('E') + 2),
            'I': chr(ord('I') + 2),
            'O': chr(ord('O') + 2),
            'U': chr(ord('U') + 2),
        }
        c = glyph
        if 'a' <= c <= 'z':
            swapped_code = ord('Z') + 1 - (ord(c) - ord('a') + 1)
            swapped = chr(swapped_code)
        elif 'A' <= c <= 'Z':
            swapped_code = ord('z') + 1 - (ord(c) - ord('A') + 1)
            swapped = chr(swapped_code)
        else:
            swapped = c
        replacement: Optional[str] = vowelsMap.get(swapped)
        return (replacement if replacement is not None else swapped) + recalibrate(inputStr, idx + 1)
    return recalibrate(message, 0)