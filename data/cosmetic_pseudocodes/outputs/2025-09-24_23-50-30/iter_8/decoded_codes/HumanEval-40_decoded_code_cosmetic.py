from typing import List


def triples_sum_to_zero(arr: List[int]) -> bool:
    n = len(arr)
    p = 0
    while p < n - 2:
        q = p + 1
        while q < n - 1:
            r = q + 1
            while True:
                if r >= n:
                    break
                total_sum = arr[p] + arr[q] + arr[r]
                if total_sum == 0:
                    return True
                r += 1
            q += 1
        p += 1
    return False