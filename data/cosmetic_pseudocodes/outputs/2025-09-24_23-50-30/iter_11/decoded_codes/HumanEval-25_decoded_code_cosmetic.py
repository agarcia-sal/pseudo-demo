from math import floor, sqrt
from typing import List

def factorize(param_a: int) -> List[int]:
    output_seq: List[int] = []
    current_div = 2
    while True:
        if not (current_div <= floor(sqrt(param_a)) + 1):
            break
        if param_a % current_div == 0:
            output_seq.append(current_div)
            param_a //= current_div
        else:
            current_div += 1
    if param_a > 1:
        output_seq.append(param_a)
    return output_seq