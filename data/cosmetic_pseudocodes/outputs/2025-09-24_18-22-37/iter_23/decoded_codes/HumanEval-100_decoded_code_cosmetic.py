from typing import List

def make_a_pile(magnitude: int) -> List[int]:
    collection: List[int] = []
    counter: int = 0
    while counter != magnitude:
        increment: int = 2 * counter
        element: int = magnitude + increment
        collection.append(element)
        counter += 1
    return collection