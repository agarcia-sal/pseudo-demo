from typing import Union

def string_sequence(n: int) -> str:
    if n < 0:
        return ""
    return " ".join(str(number) for number in range(n + 1))