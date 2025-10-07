from typing import Dict

def encode(input: str) -> str:
    shiftMap: Dict[str, str] = {}
    alphabetGroup = "AEIOUaeiou"

    # Build the shift map for vowels by shifting ASCII code by 2
    for idx in range(len(alphabetGroup)):
        currentLetter = alphabetGroup[idx]
        shiftedAscii = ord(currentLetter) + 2
        shiftedLetter = chr(shiftedAscii)
        shiftMap[currentLetter] = shiftedLetter

    swappedText = []
    for ch in input:
        if 'a' <= ch <= 'z':
            swappedText.append(ch.upper())
        elif 'A' <= ch <= 'Z':
            swappedText.append(ch.lower())
        else:
            swappedText.append(ch)
    swappedText_str = ''.join(swappedText)

    resultBuffer = []
    for element in swappedText_str:
        if element in shiftMap:
            resultBuffer.append(shiftMap[element])
        else:
            resultBuffer.append(element)

    return ''.join(resultBuffer)