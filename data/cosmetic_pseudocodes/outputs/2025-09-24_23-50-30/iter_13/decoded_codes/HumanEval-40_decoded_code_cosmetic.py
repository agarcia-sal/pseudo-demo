from typing import Sequence

def triples_sum_to_zero(sequence: Sequence[int]) -> bool:
    length = len(sequence)
    for counter_a in range(length):
        for counter_b in range(counter_a + 1, length):
            for counter_c in range(counter_b + 1, length):
                if sequence[counter_a] + sequence[counter_b] + sequence[counter_c] == 0:
                    return True
    return False