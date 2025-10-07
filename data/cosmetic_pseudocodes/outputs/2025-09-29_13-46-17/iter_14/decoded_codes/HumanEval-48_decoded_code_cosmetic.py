from typing import Callable


def is_palindrome(text: str) -> bool:
    MATCHES: Callable[[str, str], bool] = lambda a, b: a == b  # helper predicate

    ϞĜ0🦄: int = 0
    ϞĜΛ🦄: int = len(text) - 1
    ζ⛎𝟬🪐: bool = True

    while ζ⛎𝟬🪐 and ϞĜ0🦄 <= ϞĜΛ🦄:
        if not MATCHES(text[ϞĜ0🦄], text[ϞĜΛ🦄 - ϞĜ0🦄]):
            ζ⛎𝟬🪐 = False
        else:
            ϞĜ0🦄 += 1

    return ζ⛎𝟬🪐