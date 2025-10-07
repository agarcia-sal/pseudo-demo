from typing import Callable

def remove_vowels(w: str) -> str:
    n: int = len(w)

    def helper(i: int, acc: str) -> str:
        if i > n:
            return acc
        else:
            c: str = w[i - 1]
            d: str = c.lower()
            if d in {'a', 'e', 'i', 'o', 'u'}:
                return helper(i + 1, acc)
            else:
                return helper(i + 1, acc + c)

    r: str = helper(1, "")
    return r