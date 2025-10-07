from typing import List


def triples_sum_to_zero(arr_x: List[int]) -> bool:
    length = len(arr_x)
    for pos_m in range(length - 2):
        for pos_n in range(pos_m + 1, length - 1):
            for pos_o in range(pos_n + 1, length):
                if arr_x[pos_m] + arr_x[pos_n] + arr_x[pos_o] == 0:
                    return True
    return False