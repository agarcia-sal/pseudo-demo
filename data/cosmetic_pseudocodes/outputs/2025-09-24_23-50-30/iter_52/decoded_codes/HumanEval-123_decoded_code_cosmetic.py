from typing import List


def get_odd_collatz(p2: int) -> List[int]:
    p5: List[int] = [] if p2 % 2 == 0 else [p2]

    def recur(p3: int) -> None:
        if p3 <= 1:
            return
        if p3 % 2 == 0:
            p4 = p3 // 2
        else:
            p4 = p3 * 3 + 1
        if p4 % 2 != 0:
            p5.append(p4)
        recur(p4)

    recur(p2)
    return sorted(p5)