from typing import List, Tuple

def sum_product(list_of_integers: List[int]) -> Tuple[int, int]:
    def accumulate(index: int, current_sum: int, current_prod: int) -> Tuple[int, int]:
        if index >= len(list_of_integers):
            return current_sum, current_prod
        return accumulate(index + 1,
                          current_sum + list_of_integers[index],
                          current_prod * list_of_integers[index])
    return accumulate(0, 0, 1)