from typing import TypeVar, Iterable, List

T = TypeVar('T')

def unique(container: Iterable[T]) -> List[T]:
    temp_set: set[T] = set()
    for element in container:
        if element not in temp_set:
            temp_set.add(element)

    temp_list: List[T] = []
    for item in temp_set:
        temp_list.append(item)

    sorted_list: List[T] = temp_list

    i: int = 0
    while i < len(sorted_list) - 1:
        j: int = i + 1
        swapped: bool = False

        while j < len(sorted_list):
            if sorted_list[j] < sorted_list[i]:
                temp: T = sorted_list[i]
                sorted_list[i] = sorted_list[j]
                sorted_list[j] = temp
                swapped = True
            j += 1

        if not swapped:
            i += 1

    return sorted_list