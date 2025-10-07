from typing import List, Optional, Any

def next_smallest(lst: List[Any]) -> Optional[Any]:
    unique_list = []
    seen = []
    for i in range(len(lst)):
        current_element = lst[i]
        is_in_seen = False
        for j in range(len(seen)):
            if seen[j] == current_element:
                is_in_seen = True
                break
        if not is_in_seen:
            seen.append(current_element)
    unique_list = seen
    sorted_unique_list = []
    while len(unique_list) > 0:
        min_element = unique_list[0]
        min_index = 0
        for k in range(1, len(unique_list)):
            if unique_list[k] < min_element:
                min_element = unique_list[k]
                min_index = k
        sorted_unique_list.append(min_element)
        unique_list.pop(min_index)
    if len(sorted_unique_list) < 2:
        return None
    else:
        return sorted_unique_list[1]