from typing import List

def derivative(list_of_coefficients: List[int]) -> List[int]:
    def tail_recursive_compute(current_index: int, accumulated_result: List[int], remaining_coefficients: List[int]) -> List[int]:
        if not remaining_coefficients:
            return accumulated_result

        head_element = remaining_coefficients[0]
        rest_elements = remaining_coefficients[1:]

        if current_index != 0:
            next_accumulation = accumulated_result + [head_element * current_index]
        else:
            next_accumulation = accumulated_result

        return tail_recursive_compute(current_index + 1, next_accumulation, rest_elements)

    return tail_recursive_compute(1, [], list_of_coefficients)