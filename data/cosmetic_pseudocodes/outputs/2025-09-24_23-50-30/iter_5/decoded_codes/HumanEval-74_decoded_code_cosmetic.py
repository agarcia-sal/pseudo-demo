from typing import List, Sequence

def total_match(array_a: Sequence[Sequence[object]], array_b: Sequence[Sequence[object]]) -> Sequence[Sequence[object]]:
    sum_a = 0
    sum_b = 0

    index_a = 0
    while index_a < len(array_a):
        sum_a += len(array_a[index_a])
        index_a += 1

    index_b = 0
    while index_b < len(array_b):
        sum_b += len(array_b[index_b])
        index_b += 1

    if sum_a <= sum_b:
        return array_a
    else:
        return array_b