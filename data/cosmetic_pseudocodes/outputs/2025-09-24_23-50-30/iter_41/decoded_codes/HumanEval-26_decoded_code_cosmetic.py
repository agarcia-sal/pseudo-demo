from typing import List, TypeVar, Iterable
from collections import Counter

T = TypeVar('T')

def remove_duplicates(parameter_one: Iterable[T]) -> List[T]:
    def filter_elements(param_a: Iterable[T], param_b: T, param_c: Counter[T], param_d: List[T]) -> bool:
        # Keep the element if its total count is <= 1
        if param_c[param_b] <= 1:
            return True
        else:
            return False

    var_x: Counter[T] = Counter(parameter_one)
    var_y: List[T] = []
    for var_z in parameter_one:
        if filter_elements(parameter_one, var_z, var_x, var_y):
            var_y.append(var_z)
    return var_y