from typing import List

def triples_sum_to_zero(array_values: List[int]) -> bool:
    length = len(array_values)
    position_m = 0
    while position_m < length - 2:
        position_n = position_m + 1
        while position_n < length - 1:
            position_o = position_n + 1
            while position_o < length:
                if array_values[position_m] + array_values[position_n] + array_values[position_o] == 0:
                    return True
                position_o += 1
            position_n += 1
        position_m += 1
    return False