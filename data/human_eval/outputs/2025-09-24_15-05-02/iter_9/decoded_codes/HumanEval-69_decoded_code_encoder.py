from typing import List

def search(lst: List[int]) -> int:
    if not lst:
        return -1

    max_value = max(lst)
    frequency = [0] * (max_value + 1)

    for num in lst:
        frequency[num] += 1

    ans = -1
    for i in range(1, len(frequency)):
        if frequency[i] >= i:
            ans = i

    return ans