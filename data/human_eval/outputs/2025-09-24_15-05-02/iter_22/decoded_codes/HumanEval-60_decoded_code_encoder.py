from typing import Optional

def sum_to_n(integer_limit: int) -> int:
    if integer_limit < 0:
        return 0
    return (integer_limit * (integer_limit + 1)) // 2