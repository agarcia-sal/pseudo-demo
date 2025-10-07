from typing import Iterable, List, TypeVar

T = TypeVar('T')


def unique(input_collection: Iterable[T]) -> List[T]:
    temp_set = set()
    for element in input_collection:
        temp_set.add(element)
    temp_list = []
    index = 0
    temp_set_list = list(temp_set)  # to allow index-based access
    while index < len(temp_set_list):
        temp_list.append(temp_set_list[index])
        index += 1
    n = len(temp_list)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if temp_list[j] > temp_list[j + 1]:
                temp_list[j], temp_list[j + 1] = temp_list[j + 1], temp_list[j]
    return temp_list