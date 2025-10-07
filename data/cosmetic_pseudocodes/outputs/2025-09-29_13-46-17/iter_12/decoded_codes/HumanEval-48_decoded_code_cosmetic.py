from typing import Callable

def is_palindrome(text: str) -> bool:
    left: int = 0
    length: int = len(text)

    def helper(x: int, y: int, cont: Callable[[bool], bool]) -> bool:
        if x == y:
            return cont(True)
        else:
            def check_char(ch: str) -> bool:
                if ch != text[length - 1 - x]:
                    return cont(False)
                else:
                    return helper(x + 1, y, cont)
            return check_char(text[x])

    def identity(u: bool) -> bool:
        return u

    return helper(left, length // 2, identity)