from typing import Sequence

def smallest_change(sequence_of_numbers: Sequence[int]) -> int:
    def count_diff(position: int, limit: int) -> int:
        if position > limit:
            return 0
        match_flag = sequence_of_numbers[position] == sequence_of_numbers[len(sequence_of_numbers) - position - 1]
        return (0 if match_flag else 1) + count_diff(position + 1, limit)

    limit = (len(sequence_of_numbers) // 2) - 1
    return count_diff(0, limit)