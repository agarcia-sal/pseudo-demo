from typing import Dict

def encode(data: str) -> str:
    swaps: Dict[str, str] = {c: chr(ord(c) + 2) for c in "aeiouAEIOU"}

    def swapCase(text: str, position: int, accumulator: str) -> str:
        if position >= len(text):
            return accumulator
        current = text[position]
        if 'a' <= current <= 'z':
            swapped = current.upper()
        elif 'A' <= current <= 'Z':
            swapped = current.lower()
        else:
            swapped = current
        return swapCase(text, position + 1, accumulator + swapped)

    toggled = swapCase(data, 0, "")

    def replaceChars(text: str, idx: int, result: str) -> str:
        if idx == len(text):
            return result
        chr_ = text[idx]
        if chr_ in swaps:
            return replaceChars(text, idx + 1, result + swaps[chr_])
        else:
            return replaceChars(text, idx + 1, result + chr_)

    return replaceChars(toggled, 0, "")