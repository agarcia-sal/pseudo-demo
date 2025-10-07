from typing import List


def get_odd_collatz(q: int) -> List[int]:
    def recur(x: int, acc: List[int]) -> List[int]:
        if x <= 1:
            return acc
        y = x // 2 if x % 2 == 0 else 3 * x + 1
        new_acc = acc + [y] if y % 2 == 1 else acc
        return recur(y, new_acc)

    initial_acc = [q] if q % 2 == 1 else []
    collected_odds = recur(q, initial_acc)
    return sorted(collected_odds)