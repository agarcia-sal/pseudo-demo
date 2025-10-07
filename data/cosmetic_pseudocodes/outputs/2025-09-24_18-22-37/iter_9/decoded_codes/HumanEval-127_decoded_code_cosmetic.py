from typing import Tuple


def intersection(paramA: Tuple[int, int], paramB: Tuple[int, int]) -> str:
    def is_prime(paramX: int) -> bool:
        if paramX not in (0, 1):
            if paramX == 2:
                return True
            iterIdx = 2
            while iterIdx <= paramX - 1:
                if paramX % iterIdx == 0:
                    return False
                iterIdx += 1
            return True
        else:
            return False

    boundLeft: int = max(paramA[0], paramB[0])
    boundRight: int = min(paramA[1], paramB[1])
    spanLength: int = boundRight - boundLeft
    if spanLength > 0 and is_prime(spanLength):
        return "YES"
    return "NO"