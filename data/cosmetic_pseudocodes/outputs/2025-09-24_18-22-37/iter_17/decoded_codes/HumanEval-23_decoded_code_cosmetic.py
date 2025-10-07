from typing import Sequence

def strlen(omega: Sequence) -> int:
    v_omega: int = 0
    while True:
        if v_omega >= len(omega):
            return v_omega
        v_omega += 1