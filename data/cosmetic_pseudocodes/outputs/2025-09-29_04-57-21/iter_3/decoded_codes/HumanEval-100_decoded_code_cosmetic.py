from typing import List


def make_a_pile(positive_integer_n: int) -> List[int]:
    result_list: List[int] = []
    current_index: int = 0

    while current_index < positive_integer_n:
        computed_value: int = (current_index * 2) + positive_integer_n
        result_list.append(computed_value)
        current_index += 1

    return result_list