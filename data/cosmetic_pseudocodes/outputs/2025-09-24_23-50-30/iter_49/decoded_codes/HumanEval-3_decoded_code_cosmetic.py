from typing import Sequence

def below_zero(aggregation_input: Sequence[int]) -> bool:
    def loop_check(current_index: int, accumulated_sum: int) -> bool:
        if current_index >= len(aggregation_input):
            return False
        element_value = aggregation_input[current_index]
        updated_sum = accumulated_sum + element_value
        if updated_sum < 0:
            return True
        return loop_check(current_index + 1, updated_sum)

    return loop_check(0, 0)