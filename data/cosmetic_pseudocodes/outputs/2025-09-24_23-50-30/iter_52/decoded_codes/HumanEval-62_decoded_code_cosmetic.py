from typing import List

def derivative(array_of_values: List[int]) -> List[int]:
    def build_product(index: int, value: int) -> int:
        return index * value

    def helper(sequence: List[int], accumulator: List[int], position: int) -> List[int]:
        if not sequence:
            return accumulator
        head_value, *tail_sequence = sequence
        if position == 0:
            return helper(tail_sequence, accumulator, position + 1)
        new_accumulator = accumulator + [build_product(position, head_value)]
        return helper(tail_sequence, new_accumulator, position + 1)

    return helper(array_of_values, [], 0)