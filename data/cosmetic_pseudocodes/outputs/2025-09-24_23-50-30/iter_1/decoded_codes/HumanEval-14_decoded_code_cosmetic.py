from typing import List

def all_prefixes(input_string: str) -> List[str]:
    result_list: List[str] = []
    current_index: int = 0
    while current_index < len(input_string):
        result_list.append(input_string[: current_index + 1])
        current_index += 1
    return result_list