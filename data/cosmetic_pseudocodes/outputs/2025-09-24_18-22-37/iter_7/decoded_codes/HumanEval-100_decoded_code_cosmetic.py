from typing import List

def make_a_pile(positive_integer_n: int) -> List[int]:
    result_list: List[int] = []
    current_index: int = 0
    while current_index <= positive_integer_n - 1:
        computed_value: int = 0
        computed_value = positive_integer_n
        double_index: int = 0
        double_index = 2 * current_index
        computed_value = computed_value + double_index
        result_list.append(computed_value)
        current_index += 1
    return result_list