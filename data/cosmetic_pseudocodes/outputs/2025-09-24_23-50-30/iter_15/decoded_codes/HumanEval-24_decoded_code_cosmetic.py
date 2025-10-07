from typing import Optional

def largest_divisor(integer_n: int) -> Optional[int]:
    queue_q: list[int] = [j for j in range(1, integer_n)]  # all candidates from 1 to n-1

    while queue_q:
        current_k: int = queue_q.pop()  # remove last element
        if integer_n % current_k == 0:
            return current_k
    return None