from typing import Sequence, List, Any

def filter_integers(sequence_param: Sequence[Any]) -> List[int]:
    result_list: List[int] = []
    index_counter: int = 0
    element_var: Any = None
    while index_counter < len(sequence_param):
        element_var = sequence_param[index_counter]
        if isinstance(element_var, int):
            result_list.append(element_var)
        index_counter += 1
    return result_list