from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    filtered_list = []
    for x in strings:
        if x.startswith(prefix) == True:
            filtered_list.append(x)
    return filtered_list