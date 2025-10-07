from typing import List

def make_a_pile(positive_integer_n: int) -> List[int]:
    result_collection: List[int] = []
    current_index: int = 0
    while current_index < positive_integer_n:
        result_collection.append(positive_integer_n + (current_index * 2))
        current_index += 1
    return result_collection