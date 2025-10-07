from typing import List

def search(list_of_integers: List[int]) -> int:
    if not list_of_integers:
        return -1

    max_val = max(list_of_integers)
    count_map: List[int] = [0] * (max_val + 1)

    for number in list_of_integers:
        count_map[number] += 1

    result = -1
    for i in range(1, len(count_map)):
        if count_map[i] >= i:
            result = i

    return result