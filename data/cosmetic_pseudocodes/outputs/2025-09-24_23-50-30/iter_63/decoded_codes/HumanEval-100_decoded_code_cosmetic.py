from typing import List

def make_a_pile(positive_integer_n: int) -> List[int]:
    sequence_container: List[int] = []
    counter: int = 0
    while counter < positive_integer_n:
        sequence_container.append(counter * 2 + positive_integer_n)
        counter += 1
    return sequence_container