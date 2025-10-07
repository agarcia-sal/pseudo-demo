from typing import List

def filter_by_substring(container_alpha: List[str], fragment_beta: str) -> List[str]:
    output_delta: List[str] = []
    for element_sigma in container_alpha:
        if fragment_beta in element_sigma:
            output_delta.append(element_sigma)
    return output_delta