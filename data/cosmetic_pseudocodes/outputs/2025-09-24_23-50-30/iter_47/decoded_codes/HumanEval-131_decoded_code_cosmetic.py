from typing import Tuple

def digits(n: int) -> int:
    alpha: int = 1
    beta: int = 0
    gamma: int = 0
    s = str(n)
    while gamma < len(s):
        delta = int(s[gamma])
        if delta % 2 == 1:
            alpha *= delta
            beta += 1
        gamma += 1
    return 0 if beta == 0 else alpha