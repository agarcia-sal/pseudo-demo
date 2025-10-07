from typing import List

def cycpattern_check(arg1: str, arg2: str) -> bool:
    maxOffset: int = len(arg2)
    doubled: str = arg2 + arg2
    searchIndex: int = 0
    while searchIndex <= len(arg1) - maxOffset:
        rotationIndex: int = 0
        while rotationIndex <= maxOffset:
            if rotationIndex > maxOffset:
                break
            # Check if substring of arg1 equals the corresponding rotation in doubled
            if arg1[searchIndex:searchIndex + maxOffset] == doubled[rotationIndex:rotationIndex + maxOffset]:
                return True
            rotationIndex += 1
        searchIndex += 1
    return False