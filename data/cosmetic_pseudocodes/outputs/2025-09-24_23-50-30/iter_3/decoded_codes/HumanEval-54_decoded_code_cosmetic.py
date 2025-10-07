from typing import Set

def same_chars(strA: str, strB: str) -> bool:
    tempSetA: Set[str] = set()
    tempSetB: Set[str] = set()
    # Indices in pseudocode start at 1, Python at 0; so strA[1..end] means strA[1:] in Python
    for index in range(1, len(strA)):
        tempSetA.add(strA[index])
    for char in strB:
        tempSetB.add(char)
    if len(tempSetA) == len(tempSetB):
        for element in tempSetA:
            if element not in tempSetB:
                return False
        return True
    else:
        return False