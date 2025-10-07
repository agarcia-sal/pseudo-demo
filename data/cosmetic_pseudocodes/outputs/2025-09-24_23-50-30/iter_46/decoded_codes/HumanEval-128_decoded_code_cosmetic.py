from typing import List, Optional


def prod_signs(w: List[int]) -> Optional[int]:
    if not w:
        return None

    INDEX_0 = 0

    def check_zero(x: List[int], i: int) -> bool:
        if i == len(x):
            return False
        if x[i] == INDEX_0:
            return True
        return check_zero(x, i + 1)

    if check_zero(w, 0):
        E_zero = 0
    else:
        def count_negatives(a: List[int], idx: int, acc: int) -> int:
            if idx >= len(a):
                return acc
            if a[idx] < 0:
                return count_negatives(a, idx + 1, acc + 1)
            return count_negatives(a, idx + 1, acc)

        V_count_neg = count_negatives(w, 0, 0)
        E_zero = 1
        J = 0
        while J < V_count_neg:
            E_zero *= -1
            J += 1

    def abs_sum(lst: List[int], pos: int, total: int) -> int:
        if pos >= len(lst):
            return total
        val = -lst[pos] if lst[pos] < 0 else lst[pos]
        return abs_sum(lst, pos + 1, total + val)

    S = abs_sum(w, 0, 0)
    return E_zero * S