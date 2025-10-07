from typing import List

def remove_vowels(inputString: str) -> str:
    filteredCharacters: List[str] = []
    for character in inputString:
        lowerChar = character.lower()
        if lowerChar in {'a', 'e', 'i', 'o', 'u'}:
            continue
        filteredCharacters.append(character)
    resultString = ''.join(filteredCharacters)
    return resultString