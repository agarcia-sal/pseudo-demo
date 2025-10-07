from typing import List

def make_a_pile(factor: int) -> List[int]:
    output_collection: List[int] = []
    counter: int = 0
    while counter < factor:
        output_collection.append(counter * 2 + factor)
        counter += 1
    return output_collection