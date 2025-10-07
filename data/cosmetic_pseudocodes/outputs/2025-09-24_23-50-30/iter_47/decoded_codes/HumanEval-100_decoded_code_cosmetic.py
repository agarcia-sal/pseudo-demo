from typing import List

def make_a_pile(positive_integer_n: int) -> List[int]:
    transformed_list: List[int] = []
    idx: int = 0
    while idx < positive_integer_n:
        transformed_list.append(idx * 2 + positive_integer_n)
        idx += 1
    return transformed_list