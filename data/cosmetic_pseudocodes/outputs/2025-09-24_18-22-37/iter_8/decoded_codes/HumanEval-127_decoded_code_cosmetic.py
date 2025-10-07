from typing import List, Union


def intersection(argA: List[int], argB: List[int]) -> str:
    def is_prime(paramX: int) -> bool:
        if paramX == 0 or paramX == 1:
            return False
        if paramX == 2:
            return True
        counter = 2
        while counter < paramX:
            if paramX % counter == 0:
                return False
            counter += 1
        return True

    start_value: int = argA[0]
    end_value: int = argA[1]

    start_alt: int = argB[0]
    end_alt: int = argB[1]

    l_endpoint: int = start_value if start_value > start_alt else start_alt
    r_endpoint: int = end_value if end_value < end_alt else end_alt

    intersection_diff: int = r_endpoint - l_endpoint

    if intersection_diff > 0 and is_prime(intersection_diff):
        return "YES"

    return "NO"