from typing import Sequence

def triples_sum_to_zero(collection_of_numbers: Sequence[int]) -> bool:
    length = len(collection_of_numbers)
    position_alpha = 0
    while position_alpha <= length - 1:
        pointer_beta = position_alpha + 1
        while pointer_beta <= length - 1:
            iterator_gamma = pointer_beta + 1
            while iterator_gamma <= length - 1:
                partial_sum_1 = collection_of_numbers[position_alpha]
                partial_sum_2 = collection_of_numbers[pointer_beta]
                partial_sum_3 = collection_of_numbers[iterator_gamma]
                combined_total = partial_sum_1 + partial_sum_2 + partial_sum_3
                if combined_total == 0:
                    return True
                iterator_gamma += 1
            pointer_beta += 1
        position_alpha += 1
    return False