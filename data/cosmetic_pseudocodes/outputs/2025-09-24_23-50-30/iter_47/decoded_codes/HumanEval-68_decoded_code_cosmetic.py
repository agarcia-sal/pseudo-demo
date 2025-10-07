from typing import List, Union

def pluck(collection_of_nodes: List[int]) -> List[Union[int, int]]:
    if not collection_of_nodes:
        return []

    filtered_evens: List[int] = [value for value in collection_of_nodes if value % 2 == 0]
    if not filtered_evens:
        return []

    candidate_even: int = filtered_evens[0]
    for each_value in filtered_evens:
        if candidate_even > each_value:
            candidate_even = each_value

    for position, value in enumerate(collection_of_nodes):
        if value == candidate_even:
            return [candidate_even, position]

    return []