from typing import List, Any

def filter_integers(arr_input: List[Any]) -> List[int]:
    arr_result: List[int] = []
    idx: int = 0
    while idx < len(arr_input):
        current_item = arr_input[idx]
        if isinstance(current_item, int):
            arr_result.append(current_item)
        idx += 1
    return arr_result