from typing import List

def filter_by_prefix(sequence_of_terms: List[str], initial_segment: str) -> List[str]:
    outcome_list: List[str] = []
    index_counter: int = 0
    while index_counter < len(sequence_of_terms):
        candidate_term: str = sequence_of_terms[index_counter]
        if candidate_term.startswith(initial_segment):
            outcome_list.append(candidate_term)
        index_counter += 1
    return outcome_list