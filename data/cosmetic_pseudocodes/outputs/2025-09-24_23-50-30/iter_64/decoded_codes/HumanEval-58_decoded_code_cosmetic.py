from typing import List, Set


def common(paramA: List[int], paramB: List[int]) -> List[int]:
    def helper(indexX: int, indexY: int, accumulator: Set[int]) -> List[int]:
        if indexX >= len(paramA):
            return sorted(accumulator)
        if indexY >= len(paramB):
            return helper(indexX + 1, 0, accumulator)
        new_accumulator = accumulator
        if paramA[indexX] == paramB[indexY]:
            new_accumulator = accumulator | {paramA[indexX]}
        return helper(indexX, indexY + 1, new_accumulator)

    return helper(0, 0, set())