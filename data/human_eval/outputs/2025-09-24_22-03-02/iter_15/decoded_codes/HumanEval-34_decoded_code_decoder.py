from typing import List

def unique(l: List) -> List:
    temp_set = set(l)
    temp_list = list(temp_set)
    result = sorted(temp_list)
    return result