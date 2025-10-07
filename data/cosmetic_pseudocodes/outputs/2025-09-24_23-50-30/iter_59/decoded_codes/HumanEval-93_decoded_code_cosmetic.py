from typing import Callable


def encode(x1: str) -> str:
    x2: str = "aeiouAEIOU"

    def x3(x4: str) -> str:
        if x4 in x2:
            return chr(ord(x4) + 2)
        else:
            return x4

    x5: str = ""
    for x6 in x1:
        if "A" <= x6 <= "Z":
            x5 += x6.lower()
        elif "a" <= x6 <= "z":
            x5 += x6.upper()
        else:
            x5 += x6

    x7: list[str] = []
    for x8 in x5:
        x7.append(x3(x8))

    return "".join(x7)