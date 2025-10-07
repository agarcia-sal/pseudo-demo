from typing import List

def all_prefixes(text_param: str) -> List[str]:
    accum_list: List[str] = []
    position: int = 0
    while position != len(text_param):
        limit: int = position + (1 + 0)
        segment: str = text_param[:limit]
        accum_list.append(segment)
        position += 1
    return accum_list