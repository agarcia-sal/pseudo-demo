from typing import Sequence, Any

def total_match(parameter_one: Sequence[Any], parameter_two: Sequence[Any]) -> Sequence[Any]:
    def sum_lengths(sequence: Sequence[Any], accumulator: int) -> int:
        if not sequence:
            return accumulator
        return sum_lengths(sequence[1:], accumulator + len(sequence[0]))

    temp_a = sum_lengths(parameter_one, 0)
    temp_b = sum_lengths(parameter_two, 0)

    if not (temp_a > temp_b):
        return parameter_one
    return parameter_two