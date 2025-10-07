from typing import List

def all_prefixes(input_string: str) -> List[str]:
    result_list: List[str] = []
    index: int = 0
    while index < len(input_string):
        result_list.append(input_string[:index + 1])
        index += 1
    return result_list