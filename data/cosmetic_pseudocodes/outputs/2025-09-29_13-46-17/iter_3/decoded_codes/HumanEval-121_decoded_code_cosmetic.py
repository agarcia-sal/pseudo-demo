from typing import List

def solution(list_of_integers: List[int]) -> int:
    def sumOddsAtEvenIndices(currentIndex: int, totalSum: int) -> int:
        if currentIndex >= len(list_of_integers):
            return totalSum
        # Add element if index is even and element is odd
        if not ((currentIndex % 2 == 1) or (list_of_integers[currentIndex] % 2 == 0)):
            totalSum += list_of_integers[currentIndex]
        return sumOddsAtEvenIndices(currentIndex + 1, totalSum)
    return sumOddsAtEvenIndices(0, 0)