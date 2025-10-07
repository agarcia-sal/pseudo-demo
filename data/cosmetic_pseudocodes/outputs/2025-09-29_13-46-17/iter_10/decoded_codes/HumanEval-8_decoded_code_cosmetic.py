from typing import List, Tuple

def sum_product(list_of_integers: List[int]) -> Tuple[int, int]:
    def _recur(lst: List[int], acc_sum: int, acc_prod: int) -> Tuple[int, int]:
        if lst:
            head, *tail = lst
            return _recur(tail, acc_sum + head, acc_prod * head)
        return acc_sum, acc_prod
    return _recur(list_of_integers, 0, 1)