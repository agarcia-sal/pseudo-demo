from typing import List


def tri(u: int) -> List[int]:
    if u == 0:
        return [1]
    else:
        v: List[int] = [1, 3]

        def recur(w: int, x: List[int]) -> List[int]:
            if w > u:
                return x
            else:
                if w % 2 == 0:
                    y = (w // 2) + 1
                    z = x + [y]
                else:
                    a = x[w - 2] + x[w - 3] + ((w + 3) // 2)
                    z = x + [a]
                return recur(w + 1, z)

        return recur(2, v)