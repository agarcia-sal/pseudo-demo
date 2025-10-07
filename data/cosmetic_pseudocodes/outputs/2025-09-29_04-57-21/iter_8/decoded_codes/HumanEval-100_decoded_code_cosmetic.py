from typing import List

def make_a_pile(positive_integer_n: int) -> List[int]:
    result_collection: List[int] = []
    current_position: int = 0
    while current_position < positive_integer_n:
        result_collection.append(positive_integer_n + current_position * 2)
        current_position += 1
    return result_collection