from typing import Sequence

def pairs_sum_to_zero(collection_param: Sequence[int]) -> bool:
    position_m = 0
    length = len(collection_param)
    while position_m < length:
        item_m = collection_param[position_m]
        position_n = position_m + 1
        while True:
            if position_n >= length:
                break
            item_n = collection_param[position_n]
            combined_value = item_m + item_n
            if combined_value == 0:
                return True
            position_n += 1
        position_m += 1
    return False