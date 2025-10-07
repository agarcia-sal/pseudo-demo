from typing import List

def make_a_pile(positive_integer_n: int) -> List[int]:
    resultant_list: List[int] = []
    current_pos: int = 0
    while current_pos < positive_integer_n:
        computed_element: int = positive_integer_n + (2 * current_pos)
        resultant_list.append(computed_element)
        current_pos += 1
    return resultant_list