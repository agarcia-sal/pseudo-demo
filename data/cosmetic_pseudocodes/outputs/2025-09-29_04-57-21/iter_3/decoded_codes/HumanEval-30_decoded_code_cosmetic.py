from typing import List

def get_positive(list_of_numbers: List[float]) -> List[float]:
    positive_candidates: List[float] = []
    for candidate_element in list_of_numbers:
        if candidate_element <= 0:
            continue
        positive_candidates.append(candidate_element)
    return positive_candidates