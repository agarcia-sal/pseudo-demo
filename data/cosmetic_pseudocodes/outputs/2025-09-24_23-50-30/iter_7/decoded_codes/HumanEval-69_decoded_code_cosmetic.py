from typing import List

def search(array_of_numbers: List[int]) -> int:
    max_num = max(array_of_numbers) if array_of_numbers else 0
    counts: List[int] = [0] * (max_num + 1)

    def accumulateCounts(position: int) -> None:
        if position == len(array_of_numbers):
            return
        counts[array_of_numbers[position]] += 1
        accumulateCounts(position + 1)

    accumulateCounts(0)

    result: int = -1

    def findAnswer(index: int) -> None:
        nonlocal result
        if index > len(counts) - 1:
            return
        if counts[index] >= index:
            result = index
        findAnswer(index + 1)

    findAnswer(1)
    return result