from typing import Union

def solve(input_X: Union[int, str]) -> str:
    sum_accumulator: int = 0
    index_pointer: int = 0
    digits_list: str = str(input_X)
    while index_pointer < len(digits_list):
        current_element: str = digits_list[index_pointer]
        sum_accumulator += int(current_element)
        index_pointer += 1
    full_binary: str = "0b" + bin(sum_accumulator)[2:]
    binary_output: str = full_binary[2:]
    return binary_output