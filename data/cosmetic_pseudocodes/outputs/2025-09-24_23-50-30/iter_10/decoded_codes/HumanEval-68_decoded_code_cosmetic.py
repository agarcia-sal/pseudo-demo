from typing import List, Union

def pluck(collection: List[int]) -> List[Union[int]]:
    if not collection:
        return []

    filtered: List[int] = [each_element for each_element in collection if each_element % 2 == 0]

    if not filtered:
        return []

    min_candidate: int = filtered[0]
    for candidate_element in filtered:
        if candidate_element < min_candidate:
            min_candidate = candidate_element

    result_index: int = 0
    for i in range(len(collection)):
        if collection[i] == min_candidate:
            result_index = i
            break

    return [min_candidate, result_index]