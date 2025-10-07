from typing import List

def maximum(list_values: List[int], count_limit: int) -> List[int]:
    result_sequence: List[int] = []
    if count_limit == 0:
        pass  # result_sequence remains empty
    else:
        list_values.sort()
        len_values = len(list_values)
        start_pos = max(len_values - count_limit, 0)
        result_sequence = list_values[start_pos:len_values]
    return result_sequence