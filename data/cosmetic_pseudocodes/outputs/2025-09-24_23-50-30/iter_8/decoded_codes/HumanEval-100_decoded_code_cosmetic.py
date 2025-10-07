from typing import List

def make_a_pile(positive_integer_n: int) -> List[int]:
    result_list: List[int] = []
    for counter in range(positive_integer_n):
        result_list.append(2 * counter + positive_integer_n)
    return result_list