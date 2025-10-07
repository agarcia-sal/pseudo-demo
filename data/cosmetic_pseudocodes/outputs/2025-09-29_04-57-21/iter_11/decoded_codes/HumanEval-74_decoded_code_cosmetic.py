from typing import Sequence, Sized

def total_match(
    collection_alpha: Sequence[Sized],
    collection_beta: Sequence[Sized]
) -> Sequence[Sized]:
    sum_alpha: int = 0
    iterator_alpha: int = 0
    while iterator_alpha < len(collection_alpha):
        sum_alpha += len(collection_alpha[iterator_alpha])
        iterator_alpha += 1

    sum_beta: int = 0
    pointer_beta: int = 0
    while pointer_beta < len(collection_beta):
        sum_beta += len(collection_beta[pointer_beta])
        pointer_beta += 1

    if not (sum_alpha > sum_beta):
        return collection_alpha
    return collection_beta