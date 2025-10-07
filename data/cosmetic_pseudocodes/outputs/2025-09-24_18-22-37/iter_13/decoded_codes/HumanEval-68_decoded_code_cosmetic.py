from typing import Sequence, List, Union


def pluck(collection_of_elements: Sequence[int]) -> List[Union[int, int]]:
    count_of_elements: int = len(collection_of_elements)
    if count_of_elements <= 0:
        return []

    filtered_evens: List[int] = []
    position: int = 0
    while position < count_of_elements:
        element = collection_of_elements[position]
        remainder = element % 2
        if remainder == 0:
            filtered_evens.append(element)
        position += 1

    if len(filtered_evens) == 0:
        return []

    minimal_value: int = filtered_evens[0]
    iter_index: int = 1
    while iter_index < len(filtered_evens):
        if filtered_evens[iter_index] < minimal_value:
            minimal_value = filtered_evens[iter_index]
        iter_index += 1

    idx: int = 0
    found_index: int = -1
    while found_index == -1:
        if collection_of_elements[idx] == minimal_value:
            found_index = idx
            break
        idx += 1

    return [minimal_value, found_index]