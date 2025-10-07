from typing import List

def derivative(array_of_numbers: List[float]) -> List[float]:
    def helper(current_index: int, remaining_list: List[float], accumulated: List[float]) -> List[float]:
        if not remaining_list:
            return accumulated
        head_value = remaining_list[0]
        tail_values = remaining_list[1:]
        # append current term's derivative coefficient
        updated_accumulated = accumulated + [head_value * current_index]
        return helper(current_index + 1, tail_values, updated_accumulated)

    return helper(1, array_of_numbers[1:], [])