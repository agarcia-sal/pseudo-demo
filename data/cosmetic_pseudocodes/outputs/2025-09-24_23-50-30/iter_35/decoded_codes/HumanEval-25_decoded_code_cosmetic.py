from math import sqrt, floor
from typing import List

def factorize(value_m: int) -> List[int]:
    factors_collection: List[int] = []
    index_j = 2
    while True:
        if index_j > floor(sqrt(value_m)) + 1:
            break
        elif value_m % index_j == 0:
            factors_collection.append(index_j)
            value_m //= index_j
        else:
            index_j += 1
    if value_m > 1:
        factors_collection.append(value_m)
    return factors_collection