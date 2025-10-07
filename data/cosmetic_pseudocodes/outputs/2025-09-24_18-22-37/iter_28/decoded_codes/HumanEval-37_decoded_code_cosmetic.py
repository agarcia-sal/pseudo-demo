from typing import List, TypeVar

T = TypeVar('T')

def sort_even(list_of_elements: List[T]) -> List[T]:
    temp_var1: List[T] = []
    temp_var2: List[T] = []
    idx_i: int = 0
    while idx_i < len(list_of_elements):
        if idx_i % 2 == 0:
            temp_var1.append(list_of_elements[idx_i])
        else:
            temp_var2.append(list_of_elements[idx_i])
        idx_i += 1

    cmp_flag: bool = True
    while cmp_flag:
        cmp_flag = False
        pos_j = 0
        while pos_j < len(temp_var1) - 1:
            if temp_var1[pos_j] > temp_var1[pos_j + 1]:
                temp_swap = temp_var1[pos_j]
                temp_var1[pos_j] = temp_var1[pos_j + 1]
                temp_var1[pos_j + 1] = temp_swap
                cmp_flag = True
            pos_j += 1

    result_list: List[T] = []
    it_even = 0
    it_odd = 0
    while it_even < len(temp_var1) and it_odd < len(temp_var2):
        result_list.append(temp_var1[it_even])
        result_list.append(temp_var2[it_odd])
        it_even += 1
        it_odd += 1

    if len(temp_var1) > len(temp_var2):
        result_list.append(temp_var1[-1])

    return result_list