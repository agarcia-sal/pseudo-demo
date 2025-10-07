from typing import List

def sort_array(array: List[int]) -> List[int]:
    count_elements: int = len(array)
    result_list: List[int] = []
    if count_elements != 0:
        first_element: int = array[0]
        last_element: int = array[count_elements - 1]
        sum_ends: int = first_element + last_element
        parity_flag: bool = False
        if sum_ends % 2 == 0:
            parity_flag = True
        else:
            parity_flag = False
        sorted_array: List[int] = array
        if parity_flag:
            sorted_array = sorted(sorted_array, reverse=True)
        else:
            sorted_array = sorted(sorted_array)
        result_list = sorted_array
    else:
        result_list = []
    return result_list