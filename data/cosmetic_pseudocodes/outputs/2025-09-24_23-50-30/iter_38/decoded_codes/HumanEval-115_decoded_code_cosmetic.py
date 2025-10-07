import math
from typing import List


def max_fill(matrix: List[List[int]], limit: int) -> int:
    temp_list: List[int] = []
    for seq in matrix:
        total = sum(seq)
        quotient = total / limit
        ceil_val = math.ceil(quotient)
        temp_list.append(ceil_val)
    result = sum(temp_list)
    return result