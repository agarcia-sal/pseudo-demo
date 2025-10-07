from typing import List

def make_a_pile(positive_integer_n: int) -> List[int]:
    result_list: List[int] = []
    counter: int = 0
    while counter < positive_integer_n:
        result_list.append(positive_integer_n + (2 * counter))
        counter += 1
    return result_list