from typing import List

def add_elements(integer_list: List[int], k_integer: int) -> int:
    def helper(index_counter: int, accumulated_sum: int) -> int:
        if index_counter == k_integer:
            return accumulated_sum
        current_value = integer_list[index_counter]
        updated_sum = accumulated_sum
        if len(str(current_value)) <= 2:
            updated_sum += current_value
        return helper(index_counter + 1, updated_sum)
    return helper(0, 0)