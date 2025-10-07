from typing import Sequence

def triples_sum_to_zero(collection_of_numbers: Sequence[int]) -> bool:
    n = len(collection_of_numbers)
    pointer_a: int = 0
    while pointer_a < n:
        pointer_b: int = pointer_a + 1
        while pointer_b < n:
            pointer_c: int = pointer_b + 1
            while pointer_c < n:
                if (collection_of_numbers[pointer_a] +
                    collection_of_numbers[pointer_b] +
                    collection_of_numbers[pointer_c]) == 0:
                    return True
                pointer_c += 1
            pointer_b += 1
        pointer_a += 1
    return False