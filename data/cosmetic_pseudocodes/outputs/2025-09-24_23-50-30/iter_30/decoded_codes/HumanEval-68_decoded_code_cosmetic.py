from typing import List, Union

def pluck(nodes_sequence: List[int]) -> List[Union[int, str]]:
    if not nodes_sequence:
        return []

    filtered_evens: List[int] = [x for x in nodes_sequence if x % 2 == 0]

    if not filtered_evens:
        return []

    minimal_even: int = filtered_evens[0]

    for val in filtered_evens[1:]:
        if val < minimal_even:
            minimal_even = val

    candidate_indices: List[int] = [i for i, v in enumerate(nodes_sequence) if v == minimal_even]

    position_of_minimal: int = candidate_indices[0] if candidate_indices else 0

    return [minimal_even, position_of_minimal]