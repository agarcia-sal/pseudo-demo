from typing import List

def filter_by_prefix(collection_alpha: List[str], prefix_beta: str) -> List[str]:
    output_lambda: List[str] = []
    iterator_sigma: int = 0
    while iterator_sigma < len(collection_alpha):
        element_theta: str = collection_alpha[iterator_sigma]
        if not (element_theta[:len(prefix_beta)] != prefix_beta):
            output_lambda.append(element_theta)
        iterator_sigma += 1
    return output_lambda