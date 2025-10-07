from math import sqrt
from typing import List

def factorize(v_number: int) -> List[int]:
    v_result: List[int] = []
    v_candidate: int = 2
    while v_candidate <= int(sqrt(v_number)) + 1:
        if v_number % v_candidate == 0:
            v_result.append(v_candidate)
            v_number //= v_candidate
        else:
            v_candidate += 1
    if v_number > 1:
        v_result.append(v_number)
    return v_result