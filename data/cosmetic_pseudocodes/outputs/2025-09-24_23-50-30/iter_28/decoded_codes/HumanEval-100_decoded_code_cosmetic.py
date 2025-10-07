from typing import List

def make_a_pile(delta: int) -> List[int]:
    output_collection: List[int] = []
    counter: int = 0
    while counter < delta:
        output_collection.append((counter * 2) + delta)
        counter += 1
    return output_collection