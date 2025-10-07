from typing import Iterable

def double_the_difference(numbers_collection: Iterable[float]) -> int:
    total_sum: int = 0
    for element in numbers_collection:
        if element > 0:
            if int(element) % 2 != 0:
                if '.' not in str(element):
                    total_sum += int(element) * int(element)
    return total_sum