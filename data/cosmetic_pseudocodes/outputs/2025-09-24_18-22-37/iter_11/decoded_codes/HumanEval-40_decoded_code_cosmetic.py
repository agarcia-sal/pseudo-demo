from typing import Sequence


def triples_sum_to_zero(sequence_numbers: Sequence[int]) -> bool:
    pointer_a = 0
    total_length = len(sequence_numbers)
    while pointer_a < total_length - 1:
        pointer_b = pointer_a + 1
        while pointer_b < total_length - 1:
            pointer_c = pointer_b + 1
            while pointer_c < total_length - 1:
                first_val = sequence_numbers[pointer_a]
                second_val = sequence_numbers[pointer_b]
                third_val = sequence_numbers[pointer_c]
                sum_temp = first_val + second_val + third_val
                if sum_temp == 0:
                    return True
                pointer_c += 1
            pointer_b += 1
        pointer_a += 1
    return False