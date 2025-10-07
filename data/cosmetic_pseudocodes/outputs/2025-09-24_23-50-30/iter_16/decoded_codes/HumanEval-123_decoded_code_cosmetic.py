from typing import List


def get_odd_collatz(m: int) -> List[int]:
    r: List[int] = [m] if m % 2 != 0 else []

    def step(q: int, acc: List[int]) -> List[int]:
        if q <= 1:
            return acc
        next_q = q // 2 if q % 2 == 0 else q * 3 + 1
        if next_q % 2 == 1:
            return step(next_q, acc + [next_q])
        else:
            return step(next_q, acc)

    result = step(m, r)
    return sorted(result)