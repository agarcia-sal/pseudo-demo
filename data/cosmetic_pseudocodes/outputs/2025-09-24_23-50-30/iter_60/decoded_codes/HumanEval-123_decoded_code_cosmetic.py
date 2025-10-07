from typing import List


def get_odd_collatz(p: int) -> List[int]:
    def loop(q: int, r: List[int]) -> List[int]:
        if q <= 1:
            return r
        if q % 2 == 0:
            return loop(q // 2, r)
        return loop(q * 3 + 1, r + [q * 3 + 1])

    s: List[int] = [] if p % 2 == 0 else [p]
    t: List[int] = loop(p, s)

    def quicksort(u: List[int]) -> List[int]:
        if len(u) <= 1:
            return u
        pivot = u[0]
        left = quicksort([x for x in u[1:] if x < pivot])
        right = quicksort([x for x in u[1:] if x >= pivot])
        return left + [pivot] + right

    return quicksort(t)