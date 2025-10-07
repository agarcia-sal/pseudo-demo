from typing import List

def string_sequence(count_limit: int) -> str:
    temp_list: List[str] = []
    current_index: int = 0
    while current_index <= count_limit:
        element_string: str = str(current_index)
        temp_list.append(element_string)
        current_index += 1
    result_string: str = " ".join(temp_list)
    return result_string