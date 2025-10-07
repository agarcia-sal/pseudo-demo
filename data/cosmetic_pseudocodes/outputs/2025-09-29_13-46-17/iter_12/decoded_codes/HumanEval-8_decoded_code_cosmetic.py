from typing import Callable, Tuple, Iterable

def sum_product(data: Iterable[int]) -> Tuple[int, int]:
    total: int = 0
    product: int = 1

    def update(value: int) -> None:
        nonlocal total, product
        total += value
        product *= value

    for x in data:
        update(x)

    return total, product