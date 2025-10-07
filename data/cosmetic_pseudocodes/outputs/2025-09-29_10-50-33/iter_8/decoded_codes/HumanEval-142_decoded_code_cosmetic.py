from typing import Sequence, List

def sum_squares(sequence_of_numbers: Sequence[int]) -> int:
    def accumulate(position: int, collected: List[int]) -> int:
        if not (position < len(sequence_of_numbers)):
            return sum(collected)
        if position % 3 == 0:
            return accumulate(position + 1, collected + [sequence_of_numbers[position] ** 2])
        if position % 4 == 0 and position % 3 != 0:
            return accumulate(position + 1, collected + [sequence_of_numbers[position] ** 3])
        return accumulate(position + 1, collected + [sequence_of_numbers[position]])
    return accumulate(0, [])