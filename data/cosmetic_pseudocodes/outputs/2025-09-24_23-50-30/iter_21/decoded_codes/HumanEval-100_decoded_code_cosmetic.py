from typing import List

def make_a_pile(param_m: int) -> List[int]:
    result_container: List[int] = []
    counter_k: int = 0
    while counter_k < param_m:
        result_container.append(param_m + (counter_k + counter_k))
        counter_k += 1
    return result_container