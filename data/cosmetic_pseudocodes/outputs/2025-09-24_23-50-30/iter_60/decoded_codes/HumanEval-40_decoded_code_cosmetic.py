from typing import List

def triples_sum_to_zero(x: List[int]) -> bool:
    def u(v: int, w: int) -> bool:
        if w > len(x) - 1:
            return False

        def y(z: int) -> bool:
            if z > len(x) - 1:
                return u(v + 1, v + 2)
            if x[v] + x[w] + x[z] == 0:
                return True
            return y(z + 1)

        return y(w + 1)

    return u(0, 1)