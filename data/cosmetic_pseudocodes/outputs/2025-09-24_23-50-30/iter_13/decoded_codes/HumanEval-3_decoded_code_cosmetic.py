from typing import Iterable

def below_zero(collection_of_values: Iterable[int]) -> bool:
    accumulator: int = 0
    iterator = iter(collection_of_values)
    for item in iterator:
        accumulator += item
        if accumulator < 0:
            return True
    return False