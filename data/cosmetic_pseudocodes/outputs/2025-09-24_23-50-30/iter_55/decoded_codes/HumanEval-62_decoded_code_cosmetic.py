from typing import List

def derivative(auxiliary_list: List[int]) -> List[int]:
    def multiply_by_index(input_sequence: List[int], current_position: int, result_accumulator: List[int]) -> List[int]:
        if current_position == len(input_sequence):
            return result_accumulator
        # Append product of element and its index to the accumulator
        return multiply_by_index(
            input_sequence,
            current_position + 1,
            result_accumulator + [input_sequence[current_position] * current_position]
        )
    return multiply_by_index(auxiliary_list, 1, [])