from typing import List, Tuple

def sum_product(list_of_integers: List[int]) -> Tuple[int, int]:
    aggregate_sum: int = 0
    aggregate_product: int = 1

    def accumulate(elements: List[int]) -> None:
        nonlocal aggregate_sum, aggregate_product
        if not elements:
            return
        head, tail = elements[0], elements[1:]
        aggregate_sum += head
        aggregate_product *= head
        accumulate(tail)

    accumulate(list_of_integers)
    return aggregate_sum, aggregate_product