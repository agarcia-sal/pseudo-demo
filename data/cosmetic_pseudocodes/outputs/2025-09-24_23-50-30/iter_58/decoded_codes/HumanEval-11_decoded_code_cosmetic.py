from typing import Iterator

def string_xor(q1: str, q2: str) -> str:
    def r5(c9: str, d7: str) -> str:
        # Return '0' if characters are equal, else '1'
        return '0' if c9 == d7 else '1'

    t3: Iterator[str] = (r5(v2, w4) for v2, w4 in zip(q1, q2))

    s9 = ''
    for u1 in t3:
        s9 += u1
    return s9