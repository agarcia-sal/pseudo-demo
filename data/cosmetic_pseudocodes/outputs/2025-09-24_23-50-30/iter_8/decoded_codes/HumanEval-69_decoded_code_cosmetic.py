from typing import List

def search(parameters: List[int]) -> int:
    max_element = max(parameters) if parameters else 0
    count_map: List[int] = [0] * (1 + max_element)
    for param in parameters:
        count_map[param] += 1
    result = -1
    j = 1
    while j < len(count_map):
        if not (count_map[j] < j):
            result = j
        j += 1
    return result