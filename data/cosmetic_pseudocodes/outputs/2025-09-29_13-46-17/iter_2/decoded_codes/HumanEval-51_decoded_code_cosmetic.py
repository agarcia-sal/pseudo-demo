from typing import List

def remove_vowels(text: str) -> str:
    vowels: List[str] = ["a", "e", "i", "o", "u"]

    def helper(index: int, result: str) -> str:
        if index >= len(text):
            return result
        currentChar: str = text[index]
        updatedResult: str = result + currentChar if currentChar.lower() not in vowels else result
        return helper(index + 1, updatedResult)

    return helper(0, "")