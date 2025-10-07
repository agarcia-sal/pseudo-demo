from typing import List

def incr_list(p_array: List[int]) -> List[int]:
    q_list: List[int] = []
    r_index: int = 0
    while r_index < len(p_array):
        s_value: int = p_array[r_index]
        t_sum: int = s_value + 1
        q_list.append(t_sum)
        r_index += 1
    return q_list