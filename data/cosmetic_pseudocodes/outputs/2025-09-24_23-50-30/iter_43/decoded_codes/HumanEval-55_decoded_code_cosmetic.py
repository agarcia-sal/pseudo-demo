from typing import List


def fib(index_value: int) -> int:
    queue_list: List[int]  # declared but unused as per pseudocode
    prev_value_one: int
    prev_value_two: int
    current_index: int
    current_result: int

    if not (index_value == 0 or index_value == 1):
        prev_value_two = 0
        prev_value_one = 1
        current_index = 2
        while current_index - 1 < index_value:
            current_result = prev_value_one + prev_value_two
            prev_value_two = prev_value_one
            prev_value_one = current_result
            current_index += 1
        return current_result
    if index_value == 0:
        return 0
    if index_value == 1:
        return 1