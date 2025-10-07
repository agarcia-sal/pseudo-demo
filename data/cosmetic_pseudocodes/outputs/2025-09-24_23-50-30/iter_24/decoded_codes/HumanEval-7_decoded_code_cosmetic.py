from typing import List

def filter_by_substring(flag_container: List[str], reference_token: str) -> List[str]:
    accumulator: List[str] = []
    index: int = 0
    while index < len(flag_container):
        current_element = flag_container[index]
        if reference_token in current_element:
            accumulator.append(current_element)
        index += 1
    return accumulator