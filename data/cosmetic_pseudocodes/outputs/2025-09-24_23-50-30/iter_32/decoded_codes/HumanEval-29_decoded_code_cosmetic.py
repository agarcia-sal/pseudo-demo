from typing import List

def filter_by_prefix(collection_alpha: List[str], key_beta: str) -> List[str]:
    result_gamma: List[str] = []
    index_delta: int = 0
    while index_delta < len(collection_alpha):
        element_epsilon: str = collection_alpha[index_delta]
        if element_epsilon[:len(key_beta)] == key_beta:
            result_gamma.append(element_epsilon)
        index_delta += 1
    return result_gamma