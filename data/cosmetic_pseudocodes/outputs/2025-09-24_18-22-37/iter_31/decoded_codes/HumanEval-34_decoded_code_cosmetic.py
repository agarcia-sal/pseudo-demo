from typing import Sequence, TypeVar, List

T = TypeVar('T', bound=object)

def unique(sequence_parameter: Sequence[T]) -> List[T]:
    temporary_container: set[T] = set()
    for element in sequence_parameter:
        temporary_container.add(element)
    intermediate_list: List[T] = []
    for item in temporary_container:
        intermediate_list.append(item)
    result_list: List[T] = sorted(intermediate_list)
    return result_list