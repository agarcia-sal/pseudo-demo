from typing import List

def smallest_change(array_of_integers: List[int]) -> int:
    answer: int = 0
    n: int = len(array_of_integers)
    for i in range(n // 2):
        if array_of_integers[i] != array_of_integers[n - i - 1]:
            answer += 1
    return answer