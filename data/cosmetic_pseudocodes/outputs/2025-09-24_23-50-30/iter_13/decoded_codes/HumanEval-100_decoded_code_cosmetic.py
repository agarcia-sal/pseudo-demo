from typing import List

def make_a_pile(positive_integer_n: int) -> List[int]:
    result_collection: List[int] = []
    walker: int = 0
    while walker < positive_integer_n:
        result_collection.append(2 * walker + positive_integer_n)
        walker += 1
    return result_collection