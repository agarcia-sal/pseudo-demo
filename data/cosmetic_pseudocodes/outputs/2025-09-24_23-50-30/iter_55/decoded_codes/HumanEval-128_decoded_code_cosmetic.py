from typing import List, Optional


def prod_signs(p_list: List[int]) -> Optional[int]:
    if not p_list:
        return None
    if 0 in p_list:
        v_result = 0
    else:
        v_negatives = sum(v_item < 0 for v_item in p_list)
        v_result = 1
        v_count = v_negatives
        while v_count > 0:
            v_result *= -1
            v_count -= 1
    v_total = 0
    v_index = 0
    while v_index < len(p_list):
        v_total += -p_list[v_index] if p_list[v_index] < 0 else p_list[v_index]
        v_index += 1
    return v_result * v_total