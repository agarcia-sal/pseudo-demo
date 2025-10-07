from typing import List

def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    result_list: List[int] = []
    selection_flag: bool = False
    nums = list_of_integers.copy()
    while nums:
        chosen_value = min(nums) if not selection_flag else max(nums)
        result_list.append(chosen_value)
        nums.remove(chosen_value)
        selection_flag = not selection_flag
    return result_list