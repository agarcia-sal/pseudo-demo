from typing import List

def strange_sort_list(unused_param: List[int]) -> List[int]:
    accumulator: List[int] = []
    toggle_marker: bool = True
    while unused_param:
        if toggle_marker:
            temp_value: int = min(unused_param)
            accumulator.append(temp_value)
            unused_param.remove(temp_value)
            toggle_marker = False
        else:
            temp_value: int = max(unused_param)
            accumulator.append(temp_value)
            unused_param.remove(temp_value)
            toggle_marker = True
    return accumulator