from typing import Iterable, List, TypeVar, Union

T = TypeVar('T')

def sort_third(list_input: Union[Iterable[T], List[T]]) -> List[T]:
    list_input = list(list_input)
    third_indices = range(0, len(list_input), 3)
    sorted_third_elements = sorted(list_input[i] for i in third_indices)
    for idx, val in zip(third_indices, sorted_third_elements):
        list_input[idx] = val
    return list_input