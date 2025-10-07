from typing import Sequence

def triples_sum_to_zero(sequence_of_numbers: Sequence[int]) -> bool:
    length = len(sequence_of_numbers)
    # Up to index length-2 because we need at least 3 elements
    for pointer_x in range(length - 2):
        for pointer_y in range(pointer_x + 1, length - 1):
            for pointer_z in range(pointer_y + 1, length):
                partial_sum1 = sequence_of_numbers[pointer_x]
                partial_sum2 = partial_sum1 + sequence_of_numbers[pointer_y]
                total_sum = partial_sum2 + sequence_of_numbers[pointer_z]
                if total_sum == 0:
                    return True
    return False