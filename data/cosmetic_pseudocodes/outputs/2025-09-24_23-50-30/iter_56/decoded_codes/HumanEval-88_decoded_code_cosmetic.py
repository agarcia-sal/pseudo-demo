from typing import List

def sort_array(auxList: List[int]) -> List[int]:
    if len(auxList) == 0:
        return []
    firstElemSum = auxList[0] + auxList[-1]
    flag = (firstElemSum % 2) == 0
    return sorted(auxList, reverse=not flag)