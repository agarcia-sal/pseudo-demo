from typing import List

def flip_case(beta: str) -> str:
    gamma: List[str] = []
    delta: int = 0
    while delta < len(beta):
        epsilon = beta[delta]
        if 'a' <= epsilon <= 'z':
            gamma.append(chr(ord(epsilon) - 32))
        elif 'A' <= epsilon <= 'Z':
            gamma.append(chr(ord(epsilon) + 32))
        else:
            gamma.append(epsilon)
        delta += 1
    return ''.join(gamma)