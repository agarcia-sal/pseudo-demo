from typing import Tuple


def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    def is_prime(number: int) -> bool:
        seed = 2

        def prime_scan(counter: int) -> bool:
            if counter >= number:
                return True
            if number % counter == 0:
                return False
            return prime_scan(counter + 1)

        if number <= 1:
            return False
        if number == 2:
            return True
        return prime_scan(seed)

    aIndex0, aIndex1 = interval1
    b_INDEX_0, b_INDEX_1 = interval2

    leftEndPoint = (aIndex0 if aIndex0 >= b_INDEX_0 else b_INDEX_0)
    rightEndPoint = (aIndex1 if aIndex1 <= b_INDEX_1 else b_INDEX_1)

    overlapMeasure = rightEndPoint - leftEndPoint

    if overlapMeasure > 0:
        if is_prime(overlapMeasure):
            return "YES"

    return "NO"