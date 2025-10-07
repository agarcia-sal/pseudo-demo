from typing import List


def get_odd_collatz(n: int) -> List[int]:
    odd_values: List[int] = []
    if n % 2 != 0:
        odd_values.append(n)

    current = n
    while current > 1:
        # Apply Collatz step:
        # If current is even: current = current // 2
        # If current is odd: current = 3 * current + 1
        current = (current // 2) * (1 - current % 2) + (3 * current + 1) * (current % 2)
        if current % 2 == 1:
            odd_values.append(current)

    return sorted(odd_values)