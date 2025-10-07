from typing import List

def make_a_pile(positive_integer_n: int) -> List[int]:
    result_array: List[int] = []
    index_counter: int = 0
    while index_counter < positive_integer_n:
        result_array.append(2 * index_counter + positive_integer_n)
        index_counter += 1
    return result_array