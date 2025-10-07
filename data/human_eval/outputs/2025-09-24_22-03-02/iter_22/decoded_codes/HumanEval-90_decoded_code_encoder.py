from typing import List, Optional

def next_smallest(lst: List[int]) -> Optional[int]:
    temp_set: List[int] = []
    for i in range(len(lst)):
        found = False
        for j in range(len(temp_set)):
            if lst[i] == temp_set[j]:
                found = True
                break
        if not found:
            temp_set.append(lst[i])
    temp_set.sort()
    unique_list = temp_set
    if len(unique_list) < 2:
        return None
    else:
        return unique_list[1]