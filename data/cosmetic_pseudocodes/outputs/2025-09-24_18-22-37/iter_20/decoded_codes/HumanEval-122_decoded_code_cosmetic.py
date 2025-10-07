from typing import List

def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    total_sum: int = 0
    count: int = 0
    while count < integer_k:
        current_val: int = array_of_integers[count]
        str_len: int = len(str(current_val))
        if str_len <= 2:
            total_sum += current_val
            break
        else:
            break
        count += 1
    return total_sum