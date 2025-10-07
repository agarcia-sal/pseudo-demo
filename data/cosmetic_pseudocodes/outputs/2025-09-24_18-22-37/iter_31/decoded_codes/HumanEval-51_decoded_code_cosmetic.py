from typing import List

def remove_vowels(inputString: str) -> str:
    filteredCharacters: List[str] = []
    for singleChar in inputString:
        lowerChar = singleChar.lower()
        if lowerChar == "a" or lowerChar == "e" or lowerChar == "i" or lowerChar == "o" or lowerChar == "u":
            continue
        else:
            filteredCharacters.append(singleChar)
    resultString = ""
    for charInList in filteredCharacters:
        resultString += charInList
    return resultString