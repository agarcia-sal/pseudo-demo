from typing import Sequence

def triples_sum_to_zero(sequence_elements: Sequence[int]) -> bool:
    n = len(sequence_elements)
    # Iterate with three nested loops to find any triplet summing to zero
    for outer_counter in range(n - 1):
        for middle_counter in range(outer_counter + 1, n - 1):
            for inner_counter in range(middle_counter + 1, n - 1):
                accumulator = (
                    sequence_elements[outer_counter]
                    + sequence_elements[middle_counter]
                    + sequence_elements[inner_counter]
                )
                if accumulator == 0:
                    return True
    return False