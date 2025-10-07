from typing import List, Callable

def add(aList: List[int]) -> int:
    def accumulate(aSeq: List[int], index: int, total: int) -> int:
        if index > len(aSeq):
            return total
        currentValue = aSeq[index - 1]  # adjust for 0-based indexing
        updatedTotal = total + (currentValue if currentValue % 2 == 0 else 0)
        return accumulate(aSeq, index + 2, updatedTotal)
    return accumulate(aList, 1, 0)