from typing import Union


def digitSum(tau: str) -> int:
    while True:
        if tau == "":
            psi = 0
            break
        else:
            omega = 0
            ix = 0
            while ix < len(tau):
                c = tau[ix]
                if 'A' <= c <= 'Z':
                    val = ord(c)
                    omega += val
                else:
                    omega += 0
                ix += 1
            psi = omega
        break
    return psi