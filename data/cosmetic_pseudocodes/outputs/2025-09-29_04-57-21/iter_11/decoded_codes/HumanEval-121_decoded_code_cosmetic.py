from typing import List

def solution(integersArray: List[int]) -> int:
    totalValue: int = 0
    currentIndex: int = 0

    while currentIndex < len(integersArray):
        elementItem: int = integersArray[currentIndex]
        if (currentIndex % 2) == 0:
            if (elementItem % 2) != 0:
                totalValue += elementItem
        currentIndex += 1

    return totalValue