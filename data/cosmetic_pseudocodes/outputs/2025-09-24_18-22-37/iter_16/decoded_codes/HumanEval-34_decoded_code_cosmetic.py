from typing import Iterable, TypeVar, List

T = TypeVar('T')


def unique(sequence_param: Iterable[T]) -> List[T]:
    temp_set_variable = set()
    for element_var in sequence_param:
        temp_set_variable.add(element_var)

    temp_list_variable = []
    for item_var in temp_set_variable:
        temp_list_variable.append(item_var)

    sorted_result_variable = sorted(temp_list_variable)
    return sorted_result_variable