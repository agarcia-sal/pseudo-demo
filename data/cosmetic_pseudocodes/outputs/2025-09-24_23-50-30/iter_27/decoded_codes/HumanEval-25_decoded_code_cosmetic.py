from math import floor, sqrt
from typing import List

def factorize(number_x: int) -> List[int]:
    factors_collection: List[int] = []
    candidate_y = 2
    while candidate_y <= floor(sqrt(number_x)) + 1:
        if number_x % candidate_y == 0:
            factors_collection.append(candidate_y)
            number_x //= candidate_y
            # break from this iteration to re-check same candidate_y after division
            # continue loop without incrementing candidate_y
        else:
            candidate_y += 1
    if number_x > 1:
        factors_collection.append(number_x)
    return factors_collection