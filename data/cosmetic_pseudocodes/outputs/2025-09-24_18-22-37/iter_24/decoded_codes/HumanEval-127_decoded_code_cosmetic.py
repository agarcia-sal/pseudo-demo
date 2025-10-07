from typing import Sequence, Union

def intersection(interval1: Sequence[int], interval2: Sequence[int]) -> str:
    def is_prime(number: int) -> bool:
        if number == 2:
            return True
        if number <= 1:
            return False
        for divisor in range(2, number):
            if number % divisor == 0:
                return False
        return True

    valA: int = interval1[0]
    valB: int = interval2[0]
    pointLeft: int = valB if valB > valA else valA

    valC: int = interval1[1]
    valD: int = interval2[1]
    pointRight: int = valC if valC < valD else valD

    lenSegment: int = pointRight - pointLeft
    condA: bool = lenSegment > 0
    condB: bool = is_prime(lenSegment)

    if condA and condB:
        return "YES"
    else:
        return "NO"