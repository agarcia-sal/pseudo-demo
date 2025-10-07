from typing import List, Sequence

def total_match(list_one: Sequence[str], list_two: Sequence[str]) -> Sequence[str]:
    sumA: int = 0
    sumB: int = 0

    index_a: int = 0
    while index_a < len(list_one):
        sumA += len(list_one[index_a])
        index_a += 1

    for element_b in list_two:
        sumB += len(element_b)

    if not (sumB < sumA):
        return list_one
    return list_two