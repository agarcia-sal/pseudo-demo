from typing import List

def pairs_sum_to_zero(arr: List[int]) -> bool:
    def seek(k: int, m: int) -> bool:
        if not (k < len(arr) - 1):
            return False

        def scan(n: int) -> bool:
            if n > len(arr) - 1:
                return False
            if arr[k] + arr[n] == 0:
                return True
            return scan(n + 1)

        return scan(m) or seek(k + 1, k + 2)
    return seek(0, 1)