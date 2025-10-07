from typing import List, TypeVar, Sequence

T = TypeVar('T')

def unique(mixer: Sequence[T]) -> List[T]:
    gathering: List[T] = []
    lookup: set[T] = set()
    idx = 0
    while idx < len(mixer):
        current_element = mixer[idx]
        if current_element not in lookup:
            lookup.add(current_element)
            gathering.append(current_element)
        idx += 1

    temp_holder = gathering
    sorted_result: List[T] = []
    i = 0
    while i < len(temp_holder):
        key = temp_holder[i]
        j = i
        while j > 0 and key < sorted_result[j - 1]:
            if len(sorted_result) == j:
                sorted_result.append(sorted_result[j - 1])
            else:
                sorted_result[j] = sorted_result[j - 1]
            j -= 1
        if len(sorted_result) == j:
            sorted_result.append(key)
        else:
            sorted_result[j] = key
        i += 1

    return sorted_result