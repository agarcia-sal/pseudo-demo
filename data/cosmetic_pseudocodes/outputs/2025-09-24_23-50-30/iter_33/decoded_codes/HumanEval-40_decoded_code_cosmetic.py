from typing import Sequence


def triples_sum_to_zero(sequence: Sequence[int]) -> bool:
    n = len(sequence)

    def search_pairs(first_idx: int, second_idx: int, third_idx: int) -> bool:
        if first_idx >= n - 2:
            return False

        def search_third(third_idx: int) -> bool:
            if third_idx >= n:
                # Move second and third indices forward
                return search_pairs(first_idx, second_idx + 1, second_idx + 2)
            if sequence[first_idx] + sequence[second_idx] + sequence[third_idx] == 0:
                return True
            return search_third(third_idx + 1)

        if second_idx >= n - 1:
            # Move first, second, and third indices forward
            return search_pairs(first_idx + 1, first_idx + 2, first_idx + 3)
        return search_third(third_idx)

    return search_pairs(0, 1, 2)