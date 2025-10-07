from typing import List


def get_odd_collatz(q: int) -> List[int]:
    last_elements: List[int] = [] if q % 2 == 0 else [q]

    def inner_loop(x: int, acc: List[int]) -> List[int]:
        if x <= 1:
            return acc
        y = x // 2 if x % 2 == 0 else 3 * x + 1
        new_acc = acc + [y] if y % 2 == 1 else acc
        return inner_loop(y, new_acc)

    final_sequence = inner_loop(q, last_elements)
    return sorted(final_sequence)