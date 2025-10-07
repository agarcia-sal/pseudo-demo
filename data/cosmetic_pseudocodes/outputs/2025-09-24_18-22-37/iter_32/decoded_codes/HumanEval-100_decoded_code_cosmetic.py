from typing import List


def make_a_pile(alpha: int) -> List[int]:
    output_list: List[int] = []
    iterator_var: int = 0
    while iterator_var <= (alpha - 1):
        temp_val: int = alpha + (2 * iterator_var)
        output_list.append(temp_val)
        iterator_var += 1
    return output_list