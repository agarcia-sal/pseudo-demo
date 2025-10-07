from typing import List

def remove_vowels(inputString: str) -> str:
    filteredCollection: List[str] = []
    for character in inputString:
        lower_char = character.lower()
        if (
            lower_char != "a"
            and lower_char != "e"
            and lower_char != "i"
            and lower_char != "o"
            and lower_char != "u"
        ):
            filteredCollection.append(character)
    resultString = ""
    for element in filteredCollection:
        resultString += element
    return resultString