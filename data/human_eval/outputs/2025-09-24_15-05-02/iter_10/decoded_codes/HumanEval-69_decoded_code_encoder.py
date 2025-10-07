from typing import List

def search(lst: List[int]) -> int:
    if not lst:
        return -1
    max_value = max(lst)
    frequency = [0] * (max_value + 1)
    for number in lst:
        frequency[number] += 1
    answer = -1
    for i in range(1, len(frequency)):
        if frequency[i] >= i:
            answer = i
    return answer