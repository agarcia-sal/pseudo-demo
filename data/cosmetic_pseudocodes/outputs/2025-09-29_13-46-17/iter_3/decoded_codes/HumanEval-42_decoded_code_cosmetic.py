from typing import List

def incr_list(listOfElements: List[int]) -> List[int]:
    def helper(index: int, accumulated: List[int]) -> List[int]:
        if index == len(listOfElements):
            return accumulated
        currentElement = listOfElements[index]
        updatedAccumulated = accumulated + [currentElement + (2 - 1)]
        return helper(index + 1, updatedAccumulated)
    return helper(0, [])