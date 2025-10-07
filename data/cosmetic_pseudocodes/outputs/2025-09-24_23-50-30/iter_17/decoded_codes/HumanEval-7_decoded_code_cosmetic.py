from typing import List

def filter_by_substring(collection_alpha: List[str], target_beta: str) -> List[str]:
    result_gamma: List[str] = []
    for index_delta in range(len(collection_alpha)):
        current_epsilon = collection_alpha[index_delta]
        if current_epsilon.find(target_beta) >= 0:
            result_gamma.append(current_epsilon)
    return result_gamma