from typing import List

def make_a_pile(positive_integer_n: int) -> List[int]:
    result_collection: List[int] = []
    cursor: int = 0

    while cursor < positive_integer_n:
        result_collection.append(cursor * 2 + positive_integer_n)
        cursor += 1

    return result_collection