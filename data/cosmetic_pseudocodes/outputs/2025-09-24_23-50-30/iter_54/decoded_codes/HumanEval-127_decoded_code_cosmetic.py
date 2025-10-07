from typing import List

def intersection(xyz: List[int], abc: List[int]) -> str:
    def is_prime(pqr: int) -> bool:
        if pqr in (0, 1):
            return False
        if pqr == 2:
            return True
        for idx in range(2, pqr):
            if pqr % idx == 0:
                return False
        return True

    start: int = xyz[0]
    endd: int = abc[1]
    alt_start: int = abc[0]
    alt_end: int = xyz[1]

    left_bound: int = alt_start if alt_start > start else start
    right_bound: int = endd if endd < alt_end else alt_end
    length: int = right_bound - left_bound

    if length > 0 and is_prime(length):
        return "YES"
    else:
        return "NO"