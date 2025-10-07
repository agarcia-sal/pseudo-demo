from typing import Sequence, Optional

def total_match(collection_alpha: Sequence[str], collection_beta: Sequence[str]) -> Optional[Sequence[str]]:
    sum_alpha: int = 0
    iterator_alpha: int = 0
    while iterator_alpha < len(collection_alpha):
        current_str_alpha: str = collection_alpha[iterator_alpha]
        len_current_alpha: int = len(current_str_alpha)
        sum_alpha += len_current_alpha
        iterator_alpha += 1

    sum_beta: int = 0
    for index_beta in range(len(collection_beta)):
        current_str_beta: str = collection_beta[index_beta]
        len_current_beta: int = len(current_str_beta)
        sum_beta += len_current_beta

    result_collection: Optional[Sequence[str]] = None
    if sum_alpha > sum_beta:
        result_collection = collection_beta
    else:
        result_collection = collection_alpha

    return result_collection