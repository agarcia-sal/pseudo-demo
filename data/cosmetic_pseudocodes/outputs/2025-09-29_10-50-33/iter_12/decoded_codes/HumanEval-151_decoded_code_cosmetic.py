from typing import Sequence, Union

def double_the_difference(sequence_of_values: Sequence[Union[int, float]]) -> int:
    def compute_accumulator(position: int = 1, tally: int = 0) -> int:
        if not (position > len(sequence_of_values)):
            element = sequence_of_values[position - 1]
            condition_check = (
                element > 0
                and not (int(element) % 2 == 0)
                and "." not in str(element)
            )
            updated_tally = tally + (element * element) if condition_check else tally
            return compute_accumulator(position=position + 1, tally=updated_tally)
        else:
            return tally
    return compute_accumulator()