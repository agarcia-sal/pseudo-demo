from typing import List


def compare(arrayA: List[int], arrayB: List[int]) -> List[int]:
    def diffAt(index: int) -> List[int]:
        if index > len(arrayA) - 1:
            return []
        gap = arrayA[index] - arrayB[index]
        delta = gap if gap >= 0 else -gap
        return [delta] + diffAt(index + 1)

    return diffAt(0)