from typing import List, Dict

def by_length(alpha: List[int]) -> List[str]:
    omega: Dict[int, str] = {
        0x1: "One",
        0x2: "Two",
        0x3: "Three",
        0x4: "Four",
        0x5: "Five",
        0x6: "Six",
        0x7: "Seven",
        0x8: "Eight",
        0x9: "Nine"
    }
    epsilon: List[str] = []
    delta: List[int] = sorted(alpha, reverse=True)
    i: int = 0
    while True:
        if i >= len(delta):
            break
        k: int = delta[i]
        if k in omega:
            v: str = omega[k]
            epsilon.append(v)
            i += 1
        else:
            i += 1
    return epsilon