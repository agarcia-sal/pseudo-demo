from typing import List

def strange_sort_list(alpha: List[int]) -> List[int]:
    retro_list: List[int] = []
    indicator: bool = False
    while True:
        if alpha:
            indicator = not indicator
            if indicator:
                min_val = min(alpha)
                retro_list.append(min_val)
                alpha.remove(min_val)
            else:
                max_val = max(alpha)
                retro_list.append(max_val)
                alpha.remove(max_val)
        else:
            break
    return retro_list