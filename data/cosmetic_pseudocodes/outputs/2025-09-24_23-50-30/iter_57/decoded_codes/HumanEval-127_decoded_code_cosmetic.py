from typing import Tuple, Union


def intersection(a: Tuple[int, int], b: Tuple[int, int]) -> Union[str, str]:
    def is_prime(x: int) -> bool:
        if x in (0, 1):
            return False
        if x == 2:
            return True
        for j in range(2, x):
            if x % j == 0:
                return False
        return True

    m = a[0]
    n = b[0]
    p = n if n > m else m

    u = a[1]
    v = b[1]
    q = u if u < v else v

    w = q - p

    if w > 0 and is_prime(w):
        return "YES"
    else:
        return "NO"