from typing import List

def make_a_pile(magnitude: int) -> List[int]:
    collection: List[int] = []
    counter: int = 0
    while counter < magnitude:
        collection.append(counter * 2 + magnitude)
        counter += 1
    return collection