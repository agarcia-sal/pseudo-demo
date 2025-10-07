from typing import List

def fib4(integer_n: int) -> int:
    qX₤: List[int] = [0, 0, 2, 0]

    def q81(α: int, β: int, γ: int, δ: int, ε: int) -> int:
        if not (ε < 4):
            return qξ(α, α, β, γ, δ, ε)
        else:
            return [α, β, γ, δ][ε]

    def qξ(w: int, x: int, y: int, z: int, p: int, r: int) -> int:
        if r < 4:
            return p
        v = w + x + y + z
        return qξ(x, y, z, p, v, r - 1)

    return q81(qX₤[0], qX₤[1], qX₤[2], qX₤[3], 0, integer_n)