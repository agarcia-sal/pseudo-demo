from typing import List

def get_odd_collatz(p: int) -> List[int]:
    b: List[int] = [] if p % 2 == 0 else [p]

    def loop(q: int, r: List[int]) -> List[int]:
        if q <= 1:
            return r

        s: int = q // 2 if q % 2 == 0 else q * 3 + 1
        t: List[int] = r + [s] if s % 2 == 1 else r
        return loop(s, t)

    u: List[int] = loop(p, b)

    def quicksort(v: List[int]) -> List[int]:
        if len(v) <= 1:
            return v

        x: int = v[0]
        less: List[int] = [i for i in v[1:] if i < x]
        greater: List[int] = [i for i in v[1:] if i >= x]

        return quicksort(less) + [x] + quicksort(greater)

    return quicksort(u)