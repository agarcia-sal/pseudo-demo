from typing import List


def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    acc_sum: int = 0
    counter: int = 0
    while counter < integer_k:
        current_value: int = array_of_integers[counter]
        if not (len(str(current_value)) > 2):
            acc_sum += current_value
        counter += 1
    return acc_sum