from typing import Dict

def encode(inputText: str) -> str:
    alphabetMap: Dict[str, str] = {c: chr(ord(c) + 2) for c in "aeiouAEIOU"}
    swappedText = ''.join(
        ch.lower() if ch.isupper() else ch.upper()
        for ch in inputText
    )
    resultBuffer = [
        alphabetMap.get(ch, ch)
        for ch in swappedText
    ]
    return ''.join(resultBuffer)