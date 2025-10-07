from typing import Sequence

def smallest_change(sequence_of_numbers: Sequence[int]) -> int:
    result: int = 0
    limit: int = len(sequence_of_numbers) // 2
    for i in range(limit):
        left_element = sequence_of_numbers[i]
        right_element = sequence_of_numbers[len(sequence_of_numbers) - i - 1]
        if left_element != right_element:
            result += 1
    return result