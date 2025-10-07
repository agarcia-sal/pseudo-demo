from typing import Callable


def circular_shift(integer_x: int, integer_shift: int) -> str:
    υλ7: Callable[[int], str] = lambda x: str(x)
    s = υλ7(integer_shift)
    length = len(s)
    if not (integer_shift > length):
        τ3θ = length - integer_shift
        # Concatenate substring from τ3θ to end and from start to τ3θ
        return s[τ3θ:] + s[:τ3θ]
    else:
        return s[::-1]