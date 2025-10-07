from typing import List


def make_a_pile(positive_integer_n: int) -> List[int]:
    result_collection: List[int] = []
    current_index: int = 0
    while current_index < positive_integer_n:
        next_element = positive_integer_n + (2 * current_index)
        result_collection.append(next_element)
        current_index += 1
    return result_collection