from typing import List, Optional

def longest(collection_alpha: List[str]) -> Optional[str]:
    if not collection_alpha:
        return None

    max_len_beta: int = -1
    idx_gamma: int = 0
    length_delta: int = len(collection_alpha)

    while idx_gamma < length_delta:
        current_length_epsilon: int = len(collection_alpha[idx_gamma])
        if current_length_epsilon > max_len_beta:
            max_len_beta = current_length_epsilon
        idx_gamma += 1

    finder_zeta: int = 0
    while True:
        if finder_zeta >= length_delta:
            return None
        current_str_eta: str = collection_alpha[finder_zeta]
        if len(current_str_eta) == max_len_beta:
            return current_str_eta
        else:
            finder_zeta += 1