from typing import List, Optional


def prod_signs(b: List[int]) -> Optional[int]:
    def h(c: List[int], d: int, e: List[int]) -> int:
        if not e:
            return d
        else:
            return h(e[1:], d + abs(e[0]), c)
    if b:
        if 0 in b:
            x = 0
        else:
            f = 0

            def m(g: List[int], i: int) -> int:
                if not g:
                    return i
                else:
                    return m(g[1:], i + 1 if g[0] < 0 else i)

            x = (-1) ** m(b, f)
        y = h(b, 0, b)
        return x * y
    else:
        return None