from typing import List

def filter_by_prefix(collection_alpha: List[str], key_beta: str) -> List[str]:
    container_gamma: List[str] = []
    index_delta: int = 0
    while index_delta < len(collection_alpha):
        if collection_alpha[index_delta][:len(key_beta)] == key_beta:
            container_gamma.append(collection_alpha[index_delta])
        index_delta += 1
    return container_gamma