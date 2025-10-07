from typing import Dict

def encode(inputText: str) -> str:
    vowelCollection: str = "aeiouAEIOU"
    vowelMapping: Dict[str, str] = {}
    indexCounter: int = 0
    while indexCounter < len(vowelCollection):
        vowelChar = vowelCollection[indexCounter]
        vowelMapping[vowelChar] = chr(ord(vowelChar) + 2)
        indexCounter += 1

    invertedText: str = ""
    position: int = 0
    while position < len(inputText):
        currentChar = inputText[position]
        if currentChar.islower():
            invertedText += currentChar.upper()
        elif currentChar.isupper():
            invertedText += currentChar.lower()
        else:
            invertedText += currentChar
        position += 1

    resultString: str = ""
    idx: int = 0
    while idx < len(invertedText):
        chr_ = invertedText[idx]
        if chr_ in vowelCollection:
            resultString += vowelMapping[chr_]
        else:
            resultString += chr_
        idx += 1

    return resultString