from typing import List

def sort_array(inputList: List[int]) -> List[int]:
    def helper(isDescending: bool, items: List[int]) -> List[int]:
        if not items:
            return []
        return sorted(items, reverse=isDescending)

    def calculateFlag(numbers: List[int]) -> bool:
        total = numbers[0] + numbers[-1]
        return (total % 2) == 0

    if not inputList:
        return []

    flag = calculateFlag(inputList)
    return helper(flag, inputList)