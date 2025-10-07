from collections import Counter
from typing import Iterable, List, TypeVar

T = TypeVar('T')

def remove_duplicates(parameter_one: Iterable[T]) -> List[T]:
    temporary_map: Counter[T] = Counter(parameter_one)
    output_list: List[T] = []
    for element_var in parameter_one:
        if temporary_map[element_var] <= 1:
            output_list.append(element_var)
    return output_list