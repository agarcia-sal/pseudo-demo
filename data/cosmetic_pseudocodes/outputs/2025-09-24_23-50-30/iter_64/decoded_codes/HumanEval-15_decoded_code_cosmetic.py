from typing import List

def string_sequence(fresh_param_1: int) -> str:
    initial_index: int = 0
    result_list: List[str] = []

    while initial_index <= fresh_param_1:
        temp_var: str = str(initial_index)
        result_list.append(temp_var)
        initial_index += 1

    return " ".join(result_list)