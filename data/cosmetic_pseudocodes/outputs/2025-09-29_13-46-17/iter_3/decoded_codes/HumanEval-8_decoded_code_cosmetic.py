from typing import List, Tuple

def sum_product(list_of_integers: List[int]) -> Tuple[int, int]:
    sumAccumulator: int = 0
    productAccumulator: int = 1

    while True:
        if not list_of_integers:
            break
        element: int = list_of_integers.pop(0)
        productAccumulator *= element
        sumAccumulator += element

    return sumAccumulator, productAccumulator