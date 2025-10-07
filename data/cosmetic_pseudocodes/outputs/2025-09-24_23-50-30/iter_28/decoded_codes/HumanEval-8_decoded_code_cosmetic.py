from typing import List, Tuple

def sum_product(array_values: List[int]) -> Tuple[int, int]:
    def accumulator(state: Tuple[int, int], index: int) -> Tuple[int, int]:
        if index == len(array_values):
            return state
        partial_sum = state[0] + array_values[index]
        partial_product = state[1] * array_values[index]
        return accumulator((partial_sum, partial_product), index + 1)

    initial_state: Tuple[int, int] = (0, 1)
    final_state = accumulator(initial_state, 0)
    return final_state