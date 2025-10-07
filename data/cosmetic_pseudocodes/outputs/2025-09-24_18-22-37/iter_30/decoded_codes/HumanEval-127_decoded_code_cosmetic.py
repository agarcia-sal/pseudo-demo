from typing import Tuple

def intersection(tupleA: Tuple[int, int], tupleB: Tuple[int, int]) -> str:
    def is_prime(param: int) -> bool:
        if param in (0, 1):
            return False
        if param == 2:
            return True
        for divisor in range(2, param):
            if param % divisor == 0:
                return False
        return True

    start_point = tupleA[0] if tupleA[0] > tupleB[0] else tupleB[0]
    end_point = tupleA[1] if tupleA[1] < tupleB[1] else tupleB[1]

    range_diff = end_point - start_point

    if range_diff > 0 and is_prime(range_diff):
        return "YES"
    return "NO"