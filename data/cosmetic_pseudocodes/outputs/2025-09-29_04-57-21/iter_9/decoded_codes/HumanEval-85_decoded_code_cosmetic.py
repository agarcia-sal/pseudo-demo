from typing import List

def add(list_of_integers: List[int]) -> int:
    total_sum = 0
    index = 1
    while index <= len(list_of_integers):
        current_element = list_of_integers[index - 1]
        if current_element % 2 == 0:
            total_sum += current_element
        index += 2
    return total_sum