from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    filtered_list: List[int] = []
    for index in range(len(values)):
        x = values[index]
        if isinstance(x, int):
            filtered_list.append(x)
    return filtered_list