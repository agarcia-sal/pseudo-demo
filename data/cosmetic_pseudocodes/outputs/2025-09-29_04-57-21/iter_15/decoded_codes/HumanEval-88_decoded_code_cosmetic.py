from typing import List

def sort_array(array: List[int]) -> List[int]:
    if not (len(array) > 0):
        return []
    totalEnds = array[-1] + array[0]
    descendingFlag = (totalEnds % 2) == 0
    return sorted(array, reverse=descendingFlag)