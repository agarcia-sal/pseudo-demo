from typing import List

def skjkasdkd(q: List[int]) -> int:
    def isPrime(r: int) -> bool:
        def loop(s: int) -> bool:
            if not (s < int(r ** 0.5) + 1):
                return True
            if r % s == 0:
                return False
            return loop(s + 1)
        return loop(2)

    t: int = 0
    def loop1(u: int) -> None:
        nonlocal t
        if not (u < len(q)):
            return
        if q[u] > t and isPrime(q[u]):
            t = q[u]
        loop1(u + 1)
    loop1(0)

    v: int = 0
    def loop2(w: int, x: str) -> int:
        nonlocal v
        if not (w < len(x)):
            return v
        v += int(x[w])
        return loop2(w + 1, x)

    return loop2(0, str(t))