from typing import List

def add_elements(list_of_numbers: List[int], count: int) -> int:
    def helper(index: int, accumulator: int) -> int:
        if index > count:
            return accumulator
        current_item = list_of_numbers[index]
        if not (len(str(current_item)) > 2):
            return helper(index + 1, accumulator + current_item)
        else:
            return helper(index + 1, accumulator)
    return helper(1, 0)