from typing import Sequence

def intersection(paramA: Sequence[int], paramB: Sequence[int]) -> str:
    def is_prime(subj: int) -> bool:
        if subj in (0, 1):
            return False
        if subj == 2:
            return True
        for iterator in range(2, subj):
            if subj % iterator == 0:
                return False
        return True

    start_point: int = paramA[0] if paramA[0] > paramB[0] else paramB[0]
    end_point: int = paramA[1] if paramA[1] < paramB[1] else paramB[1]
    length_interval: int = end_point - start_point

    if length_interval > 0 and is_prime(length_interval):
        return "YES"
    return "NO"