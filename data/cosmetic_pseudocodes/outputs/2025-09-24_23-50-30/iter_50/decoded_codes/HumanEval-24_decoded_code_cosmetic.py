from typing import List, Optional

def largest_divisor(integer_n: int) -> Optional[int]:
    queue_stack: List[int] = [idx for idx in range(1, integer_n)]

    def helper(dividend: int, candidates: List[int]) -> Optional[int]:
        if not candidates:
            return None
        head = candidates.pop()
        if dividend - (dividend // head) * head == 0:
            return head
        return helper(dividend, candidates)

    return helper(integer_n, queue_stack)