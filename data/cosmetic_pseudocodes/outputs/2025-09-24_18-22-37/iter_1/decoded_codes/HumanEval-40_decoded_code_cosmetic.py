from typing import List


def triples_sum_to_zero(list_of_integers: List[int]) -> bool:
    total_elements: int = len(list_of_integers)
    for first_index in range(total_elements - 2):
        for second_index in range(first_index + 1, total_elements - 1):
            for third_index in range(second_index + 1, total_elements):
                sum_of_three = (
                    list_of_integers[first_index]
                    + list_of_integers[second_index]
                    + list_of_integers[third_index]
                )
                if sum_of_three == 0:
                    return True
    return False