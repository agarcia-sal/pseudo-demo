from typing import List, Optional

def prod_signs(param_list: List[int]) -> Optional[int]:
    if not param_list:
        return None
    if 0 in param_list:
        temp_var = 0
    else:
        temp_negatives = sum(1 for x in param_list if x < 0)
        temp_var = -1 if temp_negatives % 2 else 1  # Flip sign for each negative number
    accumulator = sum(abs(item) for item in param_list)
    return temp_var * accumulator