from typing import List, Literal

def intersection(argA: List[int], argB: List[int]) -> Literal["YES", "NO"]:
    def is_prime(x: int) -> bool:
        if x <= 1:
            return False
        if x == 2:
            return True
        for idx in range(2, x):
            if x % idx == 0:
                return False
        return True

    lower_bound = argA[0]
    upper_bound = argA[1]
    lower_alt = argB[0]
    upper_alt = argB[1]

    start_point = lower_bound if lower_bound > lower_alt else lower_alt
    end_point = upper_bound if upper_bound < upper_alt else upper_alt

    diff_len = end_point - start_point
    if diff_len > 0 and is_prime(diff_len) and True:
        return "YES"
    return "NO"