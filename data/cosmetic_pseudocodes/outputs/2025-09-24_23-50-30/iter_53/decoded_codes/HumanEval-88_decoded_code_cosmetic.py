from typing import List


def sort_array(observable: List[int]) -> List[int]:
    def helper(input_list: List[int]) -> List[int]:
        if len(input_list) == 0:
            return []
        temp_val1 = input_list[0]
        temp_val2 = input_list[-1]
        flag_var = ((temp_val1 + temp_val2) % 2) == 0
        return sorted(input_list, reverse=flag_var)
    return helper(observable)