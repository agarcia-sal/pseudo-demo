from typing import List

def add_elements(list_numbers: List[int], limit_value: int) -> int:
    def helper(accumulator: int, remaining_list: List[int], count: int) -> int:
        if count == 0 or not remaining_list:
            return accumulator
        head, tail = remaining_list[0], remaining_list[1:]
        if len(str(head)) <= 2:
            return helper(accumulator + head, tail, count - 1)
        else:
            return helper(accumulator, tail, count - 1)

    return helper(0, list_numbers, limit_value)