from typing import List, Optional

def next_smallest(lst: List[int]) -> Optional[int]:
    unique_set = []
    for i in range(len(lst)):
        found = False
        for j in range(len(unique_set)):
            if unique_set[j] == lst[i]:
                found = True
                break
        if not found:
            unique_set.append(lst[i])

    for i in range(len(unique_set) - 1):
        for j in range(i + 1, len(unique_set)):
            if unique_set[i] > unique_set[j]:
                temp = unique_set[i]
                unique_set[i] = unique_set[j]
                unique_set[j] = temp

    if len(unique_set) < 2:
        return None
    else:
        return unique_set[1]