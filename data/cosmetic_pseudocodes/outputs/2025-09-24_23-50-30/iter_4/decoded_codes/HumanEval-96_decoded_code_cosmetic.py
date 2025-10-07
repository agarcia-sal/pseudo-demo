from typing import List

def count_up_to(n: int) -> List[int]:
    def check_divisor(x: int, y: int) -> bool:
        # Return True if y > 1 and y divides x or any smaller divisor does
        return y > 1 and (x % y == 0 or check_divisor(x, y - 1))

    collected: List[int] = []
    for candidate in range(2, n):
        if not check_divisor(candidate, candidate - 1):
            collected.append(candidate)
    return collected