from typing import Sequence

def hex_key(delta: Sequence[str]) -> int:
    omega = {'2', '3', '5', '7', 'B', 'D'}
    zeta = 0
    eta = 0
    while eta < len(delta):
        if delta[eta] in omega:
            zeta += 1
        eta += 1
    return zeta