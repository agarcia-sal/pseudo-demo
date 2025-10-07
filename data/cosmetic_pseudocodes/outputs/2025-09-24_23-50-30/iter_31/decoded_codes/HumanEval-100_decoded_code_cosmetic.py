from typing import List

def make_a_pile(delta: int) -> List[int]:
    aggregate: List[int] = []
    iterator: int = 0
    while iterator < delta:
        element = delta + (iterator * 2)
        aggregate.append(element)
        iterator += 1
    return aggregate