from typing import List, TypeVar

T = TypeVar('T', bound='Comparable')


class Comparable:
    def __le__(self, other: object) -> bool:
        raise NotImplementedError

    def __ge__(self, other: object) -> bool:
        raise NotImplementedError


def monotonic(list_of_elements: List[T]) -> bool:
    def is_sorted_asc(index: int) -> bool:
        if index >= len(list_of_elements) - 1:
            return True
        if not (list_of_elements[index] <= list_of_elements[index + 1]):
            return False
        return is_sorted_asc(index + 1)

    def is_sorted_desc(index: int) -> bool:
        if index >= len(list_of_elements) - 1:
            return True
        if not (list_of_elements[index] >= list_of_elements[index + 1]):
            return False
        return is_sorted_desc(index + 1)

    status_flag = is_sorted_asc(0)
    if not status_flag:
        status_flag = is_sorted_desc(0)
    return status_flag