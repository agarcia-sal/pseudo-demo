from typing import List

def largest_divisor(integer_n: int) -> int:
    queue: List[int] = []
    current = integer_n - 1
    queue.append(current)
    while queue:
        candidate = queue.pop(0)
        if candidate == 0:
            continue
        # Check if integer_n is divisible by candidate
        if integer_n % candidate == 0:
            return candidate
        next_candidate = candidate - 1
        if next_candidate > 0:
            queue.append(next_candidate)
    # No divisor found, return 1 (every integer > 1 divisible by 1)
    return 1