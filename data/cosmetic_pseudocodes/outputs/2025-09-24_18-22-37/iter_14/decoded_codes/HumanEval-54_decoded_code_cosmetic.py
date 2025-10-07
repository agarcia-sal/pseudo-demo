from typing import Set


def same_chars(zeta: str, omega: str) -> bool:
    temp_a: Set[str] = set()
    temp_b: Set[str] = set()

    idx: int = 0
    while idx < len(zeta):
        temp_a.add(zeta[idx])
        idx += 1

    jdx: int = 0
    while jdx < len(omega):
        temp_b.add(omega[jdx])
        jdx += 1

    result: bool = temp_b == temp_a
    return result