from typing import TypeVar, List, Sequence

T = TypeVar('T')

def intersperse(param_array: Sequence[T], param_sep: T) -> List[T]:
    if not param_array:
        return []
    temp_output: List[T] = []
    upper_limit = len(param_array) - 1
    idx_counter = 0
    while idx_counter < upper_limit:
        current_elem = param_array[idx_counter]
        temp_output.append(current_elem)
        temp_output.append(param_sep)
        idx_counter += 1
    final_element = param_array[upper_limit]
    temp_output.append(final_element)
    return temp_output