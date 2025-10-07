from typing import List

def intersection(paramA: List[int], paramB: List[int]) -> str:
    def is_prime(localX: int) -> bool:
        if localX <= 1:
            return False
        if localX == 2:
            return True
        for index in range(2, localX):
            if localX % index == 0:
                return False
        return True

    lower_bound = paramA[0]
    upper_bound = paramA[1]
    lower_comp = paramB[0]
    upper_comp = paramB[1]

    if lower_bound < lower_comp:
        lower_bound = lower_comp
    if upper_bound > upper_comp:
        upper_bound = upper_comp

    diff = upper_bound - lower_bound
    if diff > 0 and is_prime(diff):
        return "YES"
    return "NO"