from typing import Tuple


def even_odd_palindrome(e: int) -> Tuple[int, int]:
    def is_palindrome(f: int) -> bool:
        a: str = str(f)
        b: list[str] = list(reversed(list(a)))
        return a == ''.join(b)

    def loop(j: int, x: int, y: int) -> Tuple[int, int]:
        if j > e:
            return x, y
        z: int = j % 2
        if z != 0 and is_palindrome(j):
            return loop(j + 1, x, y + 1)
        elif z == 0 and is_palindrome(j):
            return loop(j + 1, x + 1, y)
        else:
            return loop(j + 1, x, y)

    return loop(1, 0, 0)