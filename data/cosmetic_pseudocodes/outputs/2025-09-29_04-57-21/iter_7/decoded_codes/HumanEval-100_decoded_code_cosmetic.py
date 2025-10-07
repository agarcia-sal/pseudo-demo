from typing import List

def make_a_pile(positive_integer_n: int) -> List[int]:
    result_collection: List[int] = []
    counter: int = 0
    while counter < positive_integer_n:
        element: int = positive_integer_n + (counter * 2)
        result_collection.append(element)
        counter += 1
    return result_collection