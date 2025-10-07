from typing import List

def strange_sort_list(lst: List[int]) -> List[int]:
    result = []
    use_minimum = True
    lst = lst.copy()
    while lst:
        selected_value = min(lst) if use_minimum else max(lst)
        result.append(selected_value)
        lst.remove(selected_value)
        use_minimum = not use_minimum
    return result