from typing import List, Callable

def sort_array(input_list: List[int]) -> List[int]:
    def count_ones(num: int) -> int:
        bit_str: str = bin(num)[2:]
        counter_var: int = 0
        index_var: int = 0
        while index_var < len(bit_str):
            if bit_str[index_var] == '1':
                counter_var += 1
            index_var += 1
        return counter_var

    temp_list: List[int] = input_list
    temp_sorted_list: List[int] = sorted(temp_list)
    result_var: List[int] = sorted(temp_sorted_list, key=count_ones)
    return result_var