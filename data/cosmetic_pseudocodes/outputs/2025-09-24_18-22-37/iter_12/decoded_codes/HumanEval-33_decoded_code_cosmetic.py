from typing import List

def sort_third(arr_param: List[int]) -> List[int]:
    temp_list: List[int] = arr_param.copy()
    div_three_positions: List[int] = []
    temp_value: List[int] = []
    # Collect elements at indices divisible by 3
    for idx in range(len(temp_list)):
        if idx % 3 == 0:
            div_three_positions.append(temp_list[idx])
    temp_value = div_three_positions
    sorted_values: List[int] = []
    for each_element in temp_value:
        sorted_values.append(each_element)
    sorted_values.sort()
    i: int = 0
    # Replace elements at indices divisible by 3 with sorted values
    for pos in range(len(temp_list)):
        if pos % 3 == 0:
            temp_list[pos] = sorted_values[i]
            i += 1
    return temp_list