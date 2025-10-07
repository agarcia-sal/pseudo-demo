from typing import List


def specialFilter(list_of_numbers: List[int]) -> int:
    totalFound: int = 0
    indexer: int = 0
    digitsOdd = {9, 5, 3, 7, 1}

    while indexer < len(list_of_numbers):
        candidate = list_of_numbers[indexer]
        if candidate > 10:
            candidateText = str(candidate)
            frontDigit = int(candidateText[0])
            rearDigit = int(candidateText[-1])
            if frontDigit in digitsOdd and rearDigit in digitsOdd:
                totalFound += 1
        indexer += 1

    return totalFound