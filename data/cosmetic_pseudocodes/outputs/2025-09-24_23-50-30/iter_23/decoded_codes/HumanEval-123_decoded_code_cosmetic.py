from typing import Set, List


def get_odd_collatz(p: int) -> List[int]:
    q: Set[int]

    if p % 2 == 1:
        q = {p}
    else:
        q = set()

    def proceed(current: int) -> None:
        while current > 1:
            if current % 2 == 0:
                current //= 2
            else:
                current = current * 3 + 1

            if current % 2 != 0:
                q.add(current)

    proceed(p)

    return sorted(q)