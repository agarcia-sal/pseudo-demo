from typing import List

def add(arr: List[int]) -> int:
    def recur_sum(idx: int, acc: int) -> int:
        if idx > len(arr):
            return acc
        if (arr[idx - 1] % 2) == 0:
            return recur_sum(idx + 2, acc + arr[idx - 1])
        else:
            return recur_sum(idx + 2, acc)
    return recur_sum(1, 0)