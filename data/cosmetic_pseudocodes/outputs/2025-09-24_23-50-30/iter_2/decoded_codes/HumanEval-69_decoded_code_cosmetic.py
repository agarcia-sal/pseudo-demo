from typing import List, Dict

def search(list_of_integers: List[int]) -> int:
    freq_map: Dict[int, int] = {}
    highest_val: int = -1
    idx: int = len(list_of_integers) - 1

    while idx >= 0:
        num = list_of_integers[idx]
        freq_map[num] = freq_map.get(num, 0) + 1
        if num > highest_val:
            highest_val = num
        idx -= 1

    answer: int = -1
    for i in reversed(range(1, highest_val + 1)):
        count = freq_map.get(i, 0)
        if not (count < i):
            answer = i
            break

    return answer