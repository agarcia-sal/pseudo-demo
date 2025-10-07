from typing import Iterable, List, TypeVar

T = TypeVar('T')

def unique(collection_param: Iterable[T]) -> List[T]:
    temporary_set = set()
    for index_var in range(len(collection_param)):
        element_holder = collection_param[index_var]
        temporary_set.add(element_holder)
    result_list: List[T] = []
    iterator_variable = iter(temporary_set)
    while True:
        try:
            current_element = next(iterator_variable)
        except StopIteration:
            break
        result_list.append(current_element)
    sorted_result = sorted(result_list)
    return sorted_result