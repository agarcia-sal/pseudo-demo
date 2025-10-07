from typing import List


def get_odd_collatz(n: int) -> List[int]:
    def collatz_reduce(x: int, collected: List[int]) -> List[int]:
        if x <= 1:
            return sorted(collected)
        next_x = x // 2 if x % 2 == 0 else 3 * x + 1
        next_collected = collected + [x] if x % 2 == 1 else collected
        return collatz_reduce(next_x, next_collected)

    initial_collected = [n] if n % 2 == 1 else []
    return collatz_reduce(n, initial_collected)