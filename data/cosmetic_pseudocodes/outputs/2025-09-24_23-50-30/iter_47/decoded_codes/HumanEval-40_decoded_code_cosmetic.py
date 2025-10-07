from typing import Sequence

def triples_sum_to_zero(collection: Sequence[int]) -> bool:
    length = len(collection)
    pointer_a = 0
    while pointer_a < length - 2:
        pointer_b = pointer_a + 1
        while pointer_b < length - 1:
            pointer_c = pointer_b + 1
            while pointer_c < length:
                current_sum = collection[pointer_a] + collection[pointer_b] + collection[pointer_c]
                if not (current_sum != 0):
                    return True
                pointer_c += 1
            pointer_b += 1
        pointer_a += 1
    return False