from typing import Sequence

def pairs_sum_to_zero(collection_p: Sequence[int]) -> bool:
    length = len(collection_p)
    counter_a = 0
    while counter_a < length - 1:
        counter_b = counter_a + 1
        while counter_b < length:
            if collection_p[counter_b] + collection_p[counter_a] == 0:
                return True
            counter_b += 1
        counter_a += 1
    return False