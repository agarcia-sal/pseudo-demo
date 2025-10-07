from typing import Callable


def greatest_common_divisor(x1: int, y1: int) -> int:
    def helper(pq: int, rs: int) -> int:
        if rs == 0:
            return pq
        else:
            return helper(rs, pq % rs)
    return helper(x1, y1)