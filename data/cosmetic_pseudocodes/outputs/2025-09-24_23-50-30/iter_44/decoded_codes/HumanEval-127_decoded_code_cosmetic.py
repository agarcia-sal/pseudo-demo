from typing import Tuple


def intersection(inputA: Tuple[int, int], inputB: Tuple[int, int]) -> str:
    def is_prime(candidate: int) -> bool:
        if candidate in (0, 1):
            return False
        if candidate == 2:
            return True
        for iterator in range(2, candidate):
            if candidate % iterator == 0:
                return False
        return True

    start_point = inputA[0] if inputA[0] > inputB[0] else inputB[0]
    end_point = inputA[1] if inputA[1] < inputB[1] else inputB[1]
    overlap = end_point - start_point

    if overlap > 0 and is_prime(overlap):
        return "YES"
    return "NO"