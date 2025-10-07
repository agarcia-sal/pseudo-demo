from typing import Any

def string_sequence(n: int) -> str:
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        return ""
    return " ".join(str(i) for i in range(n + 1))