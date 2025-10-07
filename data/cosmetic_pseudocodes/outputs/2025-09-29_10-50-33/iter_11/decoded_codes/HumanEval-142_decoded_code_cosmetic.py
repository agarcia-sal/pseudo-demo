from typing import Sequence
from functools import reduce

def sum_squares(collection_of_numbers: Sequence[int]) -> int:
    result_holder: list[int] = []
    counter: int = 0
    length: int = len(collection_of_numbers)

    while counter < length:
        if counter % 3 == 0:
            result_holder.append(collection_of_numbers[counter] ** 2)
            counter += 1
            continue
        if counter % 4 == 0 and counter % 3 != 0:
            result_holder.append(collection_of_numbers[counter] ** 3)
            counter += 1
            continue
        result_holder.append(collection_of_numbers[counter])
        counter += 1

    return reduce(lambda accumulator, elem: accumulator + elem, result_holder, 0)