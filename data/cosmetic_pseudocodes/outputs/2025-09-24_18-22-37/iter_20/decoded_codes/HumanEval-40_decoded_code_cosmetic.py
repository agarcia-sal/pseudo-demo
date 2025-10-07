from typing import Sequence


def triples_sum_to_zero(collection_of_values: Sequence[int]) -> bool:
    length = len(collection_of_values)
    position_alpha = 0
    while position_alpha <= length - 1:
        cursor_beta = position_alpha + 1
        while cursor_beta <= length - 1:
            pointer_gamma = cursor_beta + 1
            while pointer_gamma <= length - 1:
                value_at_alpha = collection_of_values[position_alpha]
                value_at_beta = collection_of_values[cursor_beta]
                value_at_gamma = collection_of_values[pointer_gamma]

                accumulated_sum = value_at_alpha + value_at_beta + value_at_gamma

                if accumulated_sum == 0:
                    return True
                pointer_gamma += 1
            cursor_beta += 1
        position_alpha += 1
    return False