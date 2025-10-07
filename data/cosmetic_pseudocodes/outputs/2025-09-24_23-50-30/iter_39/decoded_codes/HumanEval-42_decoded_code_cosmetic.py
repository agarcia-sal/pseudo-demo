from typing import List

def incr_list(arb_param: List[int]) -> List[int]:
    arb_result: List[int] = []
    for arb_idx in range(len(arb_param)):
        arb_value: int = arb_param[arb_idx]
        arb_result.append(1 + arb_value)
    return arb_result