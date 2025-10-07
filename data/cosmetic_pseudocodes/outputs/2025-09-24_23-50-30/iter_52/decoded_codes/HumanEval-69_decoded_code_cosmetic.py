from typing import Sequence

def search(container_of_numbers: Sequence[int]) -> int:
    counts: list[int] = [0] * (max(container_of_numbers, default=0) + 1)

    def accumulateCounts(position: int) -> None:
        if position > len(container_of_numbers):
            return
        currentNumber = container_of_numbers[position - 1]
        counts[currentNumber] += 1
        accumulateCounts(position + 1)

    accumulateCounts(1)

    def findAnswer(idx: int, acc: int) -> int:
        if idx > len(counts) - 1:
            return acc
        acc2 = acc
        if counts[idx] >= idx:
            acc2 = idx
        return findAnswer(idx + 1, acc2)

    return findAnswer(1, -1)