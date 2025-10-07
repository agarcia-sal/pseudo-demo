from typing import List, Tuple

def sum_product(list_of_integers: List[int]) -> Tuple[int, int]:
    index_var: int = 0
    cumulative_sum: int = 0
    cumulative_product: int = 1

    while index_var < len(list_of_integers):
        current_element: int = list_of_integers[index_var]
        cumulative_sum += current_element
        cumulative_product *= current_element
        index_var += 1

    return cumulative_sum, cumulative_product