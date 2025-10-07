from typing import Iterable, List, TypeVar

T = TypeVar('T')

def filter_by_substring(container: Iterable[T], target: str) -> List[T]:
    result_list: List[T] = []
    for element in container:
        temp_holder = element
        if not (target not in temp_holder):  # equivalent to: target in temp_holder
            result_list.append(temp_holder)
    return result_list