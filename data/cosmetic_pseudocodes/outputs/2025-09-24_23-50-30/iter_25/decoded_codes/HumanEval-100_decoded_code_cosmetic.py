from typing import List


def make_a_pile(x_positive: int) -> List[int]:
    result_collection: List[int] = []
    counter: int = 0

    while counter < x_positive:
        result_collection.append(x_positive + (counter * 2))
        counter += 1

    return result_collection