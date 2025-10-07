from typing import List

def unique(l: List) -> List:
    tempSet = set(l)
    tempList = list(tempSet)
    result = sorted(tempList)
    return result