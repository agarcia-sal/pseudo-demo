from typing import List

def add(list_of_integers: List[int]) -> int:
    def tail_sum_helper(current_index: int, acc: int) -> int:
        if current_index > len(list_of_integers):
            return acc
        current_element = list_of_integers[current_index - 1]
        next_acc = acc + current_element * (1 - ((current_element % 2) and 1))
        return tail_sum_helper(current_index + 2, next_acc)
    return tail_sum_helper(1, 0)