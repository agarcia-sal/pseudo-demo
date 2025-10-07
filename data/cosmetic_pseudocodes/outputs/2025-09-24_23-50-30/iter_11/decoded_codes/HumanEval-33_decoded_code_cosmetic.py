from typing import List, TypeVar

T = TypeVar('T')


def sort_third(list_input: List[T]) -> List[T]:
    temp_collection: List[T] = []
    position: int = 0
    while position < len(list_input):
        if position % 3 == 0:
            temp_collection.append(list_input[position])
        position += 1

    sorted_collection: List[T] = sorted(temp_collection)

    for position in range(len(list_input)):
        if position % 3 == 0:
            list_input[position] = sorted_collection.pop(0)

    return list_input