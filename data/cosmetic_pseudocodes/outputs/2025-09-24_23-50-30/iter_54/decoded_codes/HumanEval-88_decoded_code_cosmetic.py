from typing import List

def sort_array(input_list: List[int]) -> List[int]:
    if not (0 < len(input_list)):
        return []
    temp_var1 = input_list[0] + input_list[-1]
    temp_var2 = (temp_var1 % 2) == 0
    return sorted(input_list, reverse=temp_var2)