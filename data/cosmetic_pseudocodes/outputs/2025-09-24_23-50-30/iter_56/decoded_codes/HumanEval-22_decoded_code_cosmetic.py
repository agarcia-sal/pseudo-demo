from typing import List, Any

def filter_integers(param1: List[Any]) -> List[int]:
    def inner_filter(param2: List[Any], param3: int, param4: List[int]) -> List[int]:
        if param3 < len(param2):
            if isinstance(param2[param3], int):
                return inner_filter(param2, param3 + 1, param4 + [param2[param3]])
            else:
                return inner_filter(param2, param3 + 1, param4)
        else:
            return param4
    return inner_filter(param1, 0, [])