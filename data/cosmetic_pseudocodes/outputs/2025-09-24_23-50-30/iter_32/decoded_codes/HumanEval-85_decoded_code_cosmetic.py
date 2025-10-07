from typing import List

def add(list_of_integers: List[int]) -> int:
    result: int = 0
    index: int = 1
    while index <= len(list_of_integers):
        # Adjust for 1-based index in pseudocode to 0-based in Python
        if list_of_integers[index - 1] % 2 == 0:
            result += list_of_integers[index - 1]
        index += 2
    return result