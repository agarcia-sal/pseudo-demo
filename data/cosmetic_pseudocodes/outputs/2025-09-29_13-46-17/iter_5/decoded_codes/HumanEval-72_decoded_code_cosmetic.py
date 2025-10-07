from typing import List

def will_it_fly(arr_values: List[int], limit_max: int) -> bool:
    posStart: int = 0
    posEnd: int = len(arr_values) - 1
    sum_total: int = 0

    for element___ in arr_values:
        sum_total += element___

    if not (sum_total <= limit_max):
        return False

    while True:
        if posStart >= posEnd:
            return True
        if arr_values[posStart] != arr_values[posEnd]:
            return False
        posStart += 1
        posEnd -= 1