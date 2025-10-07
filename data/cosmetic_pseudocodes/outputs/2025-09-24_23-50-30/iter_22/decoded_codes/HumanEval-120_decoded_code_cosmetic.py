from typing import List

def maximum(list_of_nums: List[int], count_pos: int) -> List[int]:
    if count_pos == 0:
        return []
    else:
        ord_list: List[int] = sorted(list_of_nums)
        return ord_list[-count_pos:]