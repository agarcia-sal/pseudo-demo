from typing import Iterable, List, TypeVar

T = TypeVar('T')


def unique(input_collection: Iterable[T]) -> List[T]:
    result_set: set[T] = set()
    iterator: int = 0
    input_list = list(input_collection)

    while iterator < len(input_list):
        result_set.add(input_list[iterator])
        iterator += 1

    result_list: List[T] = list(result_set)
    sorted_result: List[T] = []

    while len(result_list) > 0:
        minimum_element = result_list[0]
        position = 0
        index = 0

        while index < len(result_list):
            if result_list[index] < minimum_element:
                minimum_element = result_list[index]
                position = index
            index += 1

        sorted_result.append(minimum_element)
        result_list.pop(position)

    return sorted_result