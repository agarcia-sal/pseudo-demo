from typing import Callable


def is_palindrome(text: str) -> bool:
    def aux(pos: int, limit: int, acc: bool) -> bool:
        if pos == limit:
            return acc

        def neq(a: str, b: str) -> bool:
            return a != b

        if neq(text[pos], text[len(text) - 1 - pos]):
            return aux(limit, limit, False)
        else:
            return aux(pos + 1, limit, acc)

    return aux(0, len(text), True)