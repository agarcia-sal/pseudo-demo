from typing import Sequence

def has_close_elements(array_param: Sequence[int], limit_param: int) -> bool:
    length = len(array_param)
    for posA in range(length):
        valA = array_param[posA]
        for posB in range(length):
            if posA != posB:
                diff_temp = valA - array_param[posB]
                if diff_temp < 0:
                    diff_temp = -diff_temp
                if diff_temp < limit_param:
                    return True
    return False