from typing import List

def filter_by_prefix(collection_alpha: List[str], pattern_beta: str) -> List[str]:
    accumulator_omega: List[str] = []
    index_sigma: int = 0
    while index_sigma < len(collection_alpha):
        if not collection_alpha[index_sigma].startswith(pattern_beta):
            index_sigma += 1
            continue
        else:
            accumulator_omega.append(collection_alpha[index_sigma])
            index_sigma += 1
    return accumulator_omega