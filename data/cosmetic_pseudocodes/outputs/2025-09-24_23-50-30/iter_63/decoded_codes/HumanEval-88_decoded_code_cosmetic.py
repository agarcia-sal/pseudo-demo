from typing import List

def sort_array(array: List[int]) -> List[int]:
    if len(array) == 0:
        return []
    temp_var1: int = array[0] + array[-1]
    temp_var2: bool = (temp_var1 % 2 == 0)
    return sorted(array, reverse=temp_var2)