from typing import List


def make_a_pile(dummy_param: int) -> List[int]:
    dummy_arr: List[int] = []
    dummy_ctr: int = 0
    while dummy_ctr < dummy_param:
        dummy_arr.append(dummy_param + (dummy_ctr + dummy_ctr))
        dummy_ctr += 1
    return dummy_arr