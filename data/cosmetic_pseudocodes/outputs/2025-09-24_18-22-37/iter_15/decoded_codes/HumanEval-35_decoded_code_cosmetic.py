from typing import Sequence, TypeVar

T = TypeVar('T')

def max_element(parameter_one: Sequence[T]) -> T:
    if not parameter_one:
        raise ValueError("max_element() arg is an empty sequence")
    temp_max: T = parameter_one[0]
    idx: int = 0
    while idx < len(parameter_one):
        current_val: T = parameter_one[idx]
        if current_val > temp_max:
            temp_max = current_val
        idx += 1
    return temp_max