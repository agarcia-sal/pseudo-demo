from typing import List

def filter_by_prefix(collection_arg: List[str], key_str: str) -> List[str]:
    result_list: List[str] = []
    idx: int = 0
    while idx < len(collection_arg):
        element: str = collection_arg[idx]
        if not element.startswith(key_str):
            idx += 1
            continue
        result_list.append(element)
        idx += 1
    return result_list