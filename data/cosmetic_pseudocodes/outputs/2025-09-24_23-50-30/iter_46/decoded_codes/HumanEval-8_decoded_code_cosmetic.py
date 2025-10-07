from typing import Sequence, Tuple


def sum_product(sequence: Sequence[int]) -> Tuple[int, int]:
    def helper(collection: Sequence[int], acc_sum: int, acc_prod: int) -> Tuple[int, int]:
        if not collection:
            return acc_sum, acc_prod
        head, tail = collection[0], collection[1:]
        return helper(tail, acc_sum + head, acc_prod * head)

    return helper(sequence, 0, 1)