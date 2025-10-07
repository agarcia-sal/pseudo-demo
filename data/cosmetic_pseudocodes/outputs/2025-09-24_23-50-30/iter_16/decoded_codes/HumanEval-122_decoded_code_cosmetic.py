from typing import List


def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    sum_accumulator: int = 0
    index_counter: int = 0

    while not (index_counter >= integer_k):
        current_value = array_of_integers[index_counter]
        if not (len(str(current_value)) > 2):
            sum_accumulator += current_value
        index_counter += 1

    return sum_accumulator