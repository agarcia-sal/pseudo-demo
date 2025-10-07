from typing import Dict

def encode(plaintext: str) -> str:
    vowelChars: str = "aeiouAEIOU"
    transformedChars: Dict[str, str] = {}
    idx: int = 0
    while idx < len(vowelChars):
        originalChar = vowelChars[idx]
        asciiVal = ord(originalChar)
        shiftedVal = asciiVal + 2
        newChar = chr(shiftedVal)
        transformedChars[originalChar] = newChar
        idx += 1

    swappedText = []
    position = 0
    while position < len(plaintext):
        ch = plaintext[position]
        if 'a' <= ch <= 'z':
            swappedText.append(chr(ord(ch) - 32))  # lower to upper
        elif 'A' <= ch <= 'Z':
            swappedText.append(chr(ord(ch) + 32))  # upper to lower
        else:
            swappedText.append(ch)
        position += 1
    swappedText_str = "".join(swappedText)

    resultText = []
    for character in swappedText_str:
        if character in transformedChars:
            resultText.append(transformedChars[character])
        else:
            resultText.append(character)
    return "".join(resultText)