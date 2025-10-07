from typing import Sequence


def triples_sum_to_zero(collection: Sequence[int]) -> bool:
    length = len(collection)
    for pos in range(length - 2):
        for q in range(pos + 1, length - 1):
            for r in range(q + 1, length):
                if collection[pos] + collection[q] + collection[r] == 0:
                    return True
    return False