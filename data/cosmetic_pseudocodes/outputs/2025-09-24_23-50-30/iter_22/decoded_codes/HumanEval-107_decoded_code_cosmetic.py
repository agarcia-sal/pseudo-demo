from typing import Optional, Tuple


def even_odd_palindrome(w: int) -> Tuple[int, int]:
    def is_palindrome(x: int) -> bool:
        s: str = str(x)
        return s == s[::-1]

    a: int = 0
    b: int = 0

    def loop(j: int) -> Optional[None]:
        nonlocal a, b
        if j > w:
            return None
        if is_palindrome(j):
            if j % 2 == 0:
                a += 1
            else:
                b += 1
        return loop(j + 1)

    loop(1)
    return a, b