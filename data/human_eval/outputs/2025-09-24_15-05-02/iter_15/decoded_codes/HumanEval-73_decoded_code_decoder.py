from typing import List

def smallest_change(array_of_integers: List[int]) -> int:
    ans = 0
    n = len(array_of_integers)
    for index in range(n // 2):
        if array_of_integers[index] != array_of_integers[n - index - 1]:
            ans += 1
    return ans