from typing import Iterable, List, TypeVar

T = TypeVar('T')


def sort_third(collection_param: Iterable[T]) -> List[T]:
    working_collection: List[T] = list(collection_param)
    positions_with_mod_three_zero: List[int] = []
    corresponding_elements: List[T] = []

    def gather_indices(index: int, max_index: int) -> None:
        if index > max_index:
            return
        positions_with_mod_three_zero.append(index)
        gather_indices(index + 3, max_index)

    gather_indices(0, len(working_collection) - 1)

    for position in positions_with_mod_three_zero:
        corresponding_elements.append(working_collection[position])

    corresponding_elements.sort()

    counter = 0
    for position in positions_with_mod_three_zero:
        working_collection[position] = corresponding_elements[counter]
        counter += 1

    return working_collection