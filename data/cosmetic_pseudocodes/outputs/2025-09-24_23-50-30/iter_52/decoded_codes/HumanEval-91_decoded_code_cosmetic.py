import re
from typing import List

def is_bored(eta: str) -> int:
    delta: List[str] = re.split(r'[.?!]\s*', eta)

    def helper(theta: List[str], accumulator: int) -> int:
        if not theta:
            return accumulator
        head, tail = theta[0], theta[1:]
        if head.startswith('I '):
            return helper(tail, accumulator + 1)
        else:
            return helper(tail, accumulator)

    return helper(delta, 0)