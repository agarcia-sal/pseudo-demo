from typing import List

def all_prefixes(input_string: str) -> List[str]:
    result_list: List[str] = []
    index_tracker: int = 0

    while index_tracker < len(input_string):
        result_list.append(input_string[0 : index_tracker + 1])
        index_tracker += 1

    return result_list