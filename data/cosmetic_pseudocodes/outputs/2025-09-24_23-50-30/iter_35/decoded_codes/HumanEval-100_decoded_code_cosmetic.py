from typing import List

def make_a_pile(count_positive_integer: int) -> List[int]:
    final_collection: List[int] = []
    iterator_var: int = 0
    while iterator_var < count_positive_integer:
        final_collection.append(count_positive_integer + (iterator_var * 2))
        iterator_var += 1
    return final_collection