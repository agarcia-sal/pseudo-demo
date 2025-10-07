from typing import List

def filter_by_substring(collection_alpha: List[str], target_beta: str) -> List[str]:
    result_gamma: List[str] = []
    index_delta: int = 0

    while index_delta < len(collection_alpha):
        current_epsilon: str = collection_alpha[index_delta]
        if target_beta in current_epsilon:
            result_gamma.append(current_epsilon)
        index_delta += 1

    return result_gamma