from typing import List

def concatenate(list_of_strings: List[str]) -> str:
    mergedString: str = ""
    iterator: int = 0
    while iterator < len(list_of_strings):
        mergedString += list_of_strings[iterator]
        iterator += 1
    return mergedString