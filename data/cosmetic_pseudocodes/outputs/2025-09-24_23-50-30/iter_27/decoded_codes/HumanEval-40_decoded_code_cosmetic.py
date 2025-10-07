from typing import Sequence

def triples_sum_to_zero(sequence_numbers: Sequence[int]) -> bool:
    length = len(sequence_numbers)
    counter_a = 0
    while counter_a <= length - 1:
        counter_b = counter_a + 1
        while counter_b <= length - 1:
            counter_c = counter_b + 1
            while counter_c <= length - 1:
                if sequence_numbers[counter_a] + sequence_numbers[counter_b] + sequence_numbers[counter_c] == 0:
                    return True
                counter_c += 1
            counter_b += 1
        counter_a += 1
    return False