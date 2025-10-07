from functools import reduce
from operator import add
from typing import List

def sum_squares(list_of_integers: List[int]) -> int:
    aggregation: List[int] = []

    def process_element(current_position: int) -> None:
        val = list_of_integers[current_position]
        if current_position % 3 == 0:
            aggregation.append(val ** 2)
        else:
            if current_position % 4 == 0:
                aggregation.append(val ** 3)
            else:
                aggregation.append(val)

    cursor = 0
    while cursor < len(list_of_integers):
        process_element(cursor)
        cursor += 1

    return reduce(add, aggregation, 0)