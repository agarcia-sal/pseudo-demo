from typing import List

def get_positive(list_of_numbers: List[int]) -> List[int]:
    result_stack: List[int] = []
    i: int = len(list_of_numbers)
    while i > 0:
        i -= 1
        if not (list_of_numbers[i] <= 0):
            result_stack.append(list_of_numbers[i])
    positive_list: List[int] = []
    while result_stack:
        positive_list.append(result_stack.pop())
    return positive_list