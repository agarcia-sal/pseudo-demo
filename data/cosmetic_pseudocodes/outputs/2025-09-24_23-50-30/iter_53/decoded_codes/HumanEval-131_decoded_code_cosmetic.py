from typing import Union


def digits(q: Union[int, str]) -> int:
    a: int = 0
    b: int = 1
    q_str: str = str(q)
    while a < len(q_str):
        c: int = int(q_str[a])
        if c % 2 != 0:
            b *= c
            a += 1  # Effects of the pseudocode increments consolidated here
            # The pseudocode has many redundant increments and no-ops on a, d, e, f, g, h
            # which have no effect on final logic; they are ignored for clarity and efficiency
        else:
            a += 1
    return 0 if b == 1 else b