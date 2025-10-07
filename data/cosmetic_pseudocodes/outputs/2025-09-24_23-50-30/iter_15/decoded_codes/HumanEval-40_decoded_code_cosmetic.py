from typing import Sequence

def triples_sum_to_zero(sequence_of_numbers: Sequence[int]) -> bool:
    length = len(sequence_of_numbers)
    outer_counter = 0
    while outer_counter <= length - 1:
        middle_counter = outer_counter + 1
        while middle_counter <= length - 1:
            inner_counter = middle_counter + 1
            while inner_counter <= length - 1:
                temp_sum = (
                    sequence_of_numbers[outer_counter] +
                    sequence_of_numbers[middle_counter] +
                    sequence_of_numbers[inner_counter]
                )
                if temp_sum == 0:
                    return True
                inner_counter += 1
            middle_counter += 1
        outer_counter += 1
    return False