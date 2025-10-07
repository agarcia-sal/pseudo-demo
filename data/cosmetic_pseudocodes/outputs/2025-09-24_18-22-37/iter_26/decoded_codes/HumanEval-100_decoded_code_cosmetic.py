from typing import List

def make_a_pile(positive_integer_n: int) -> List[int]:
    accumulator: List[int] = []
    iterator: int = 0
    while iterator < positive_integer_n:
        temp1: int = 2
        temp2: int = iterator
        temp3: int = temp1 * temp2
        temp4: int = positive_integer_n + temp3
        accumulator.append(temp4)
        iterator += 1
    return accumulator