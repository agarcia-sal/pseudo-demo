from typing import List, Union


def pluck(c: List[int]) -> List[Union[int, int]]:
    if len(c) == 0:
        return []

    def f(g: List[int], h: List[int], i: int) -> List[int]:
        if i == len(h):
            return g
        else:
            if h[i] % 2 == 0:
                return f(g + [h[i]], h, i + 1)
            else:
                return f(g, h, i + 1)

    j = f([], c, 0)

    if len(j) == 0:
        return []

    k = j[0]
    l = 0
    m = 1
    while m < len(j):
        if j[m] < k:
            k = j[m]
            l = m
        m += 1

    n = 0
    while n < len(c):
        if c[n] == k:
            return [k, n]
        n += 1

    return []