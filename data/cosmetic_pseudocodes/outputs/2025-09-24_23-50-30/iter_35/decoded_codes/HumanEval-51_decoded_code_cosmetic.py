from typing import List

def remove_vowels(data: str) -> str:
    outputList: List[str] = []
    pos: int = 0
    while pos < len(data):
        currentChar: str = data[pos]
        if currentChar.lower() in {'a', 'e', 'i', 'o', 'u'}:
            pass  # skip vowels
        else:
            outputList.append(currentChar)
        pos += 1
    return ''.join(outputList)