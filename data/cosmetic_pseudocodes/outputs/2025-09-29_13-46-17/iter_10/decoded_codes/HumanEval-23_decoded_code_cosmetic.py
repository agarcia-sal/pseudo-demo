from typing import Callable

def strlen(string: str) -> int:
    def ζ₄₁₉▽(ζₓ: str) -> int:
        if ζₓ == '':
            return 0
        else:
            return 1 + ζ₄₁₉▽(ζₓ[1:])
    return ζ₄₁₉▽(string)