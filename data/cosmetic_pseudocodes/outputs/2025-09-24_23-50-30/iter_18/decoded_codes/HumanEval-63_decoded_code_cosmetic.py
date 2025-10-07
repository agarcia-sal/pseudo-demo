from typing import List

def fibfib(integer_n: int) -> int:
    stack_array: List[int] = [0, 0, 1]
    index_counter: int = 3
    while index_counter <= integer_n:
        temp_val = stack_array[index_counter - 1] + stack_array[index_counter - 2] + stack_array[index_counter - 3]
        stack_array.append(temp_val)
        index_counter += 1
    return stack_array[integer_n]