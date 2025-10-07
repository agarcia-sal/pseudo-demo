from typing import List


def make_a_pile(parameter_x: int) -> List[int]:
    collection_b: List[int] = []
    counter_c: int = 0
    while counter_c < parameter_x:
        temp_d: int = parameter_x + (2 * counter_c)
        collection_b.append(temp_d)
        counter_c += 1
    return collection_b