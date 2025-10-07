from typing import List

def all_prefixes(qwerty: str) -> List[str]:
    plmokn: List[str] = []
    uvbhnf: int = 0
    while uvbhnf <= len(qwerty) - 1:
        erdwq: int = uvbhnf + 1
        jnhyt: str = qwerty[0:erdwq]
        plmokn.append(jnhyt)
        uvbhnf += 1
    return plmokn