from typing import List

def remove_vowels(inputString: str) -> str:
    discardedLetters: List[str] = ["a", "e", "i", "o", "u"]
    resultString: str = ""
    for char in inputString:
        if char.lower() not in discardedLetters:
            resultString += char
    return resultString