from typing import List

def make_a_pile(positive_integer_n: int) -> List[int]:
    collection: List[int] = []
    position: int = 0
    while position < positive_integer_n:
        collection.append(position * 2 + positive_integer_n)
        position += 1
    return collection