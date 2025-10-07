from typing import List

def concatenate(an_array: List[str]) -> str:
    combinedText: str = ""
    index: int = 0
    while index < len(an_array):
        currentString: str = an_array[index]
        combinedText += currentString
        index += 1
    return combinedText