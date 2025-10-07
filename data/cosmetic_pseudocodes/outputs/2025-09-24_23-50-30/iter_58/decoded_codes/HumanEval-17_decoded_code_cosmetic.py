from typing import List

def parse_music(k1: str) -> List[int]:
    k2: dict[str, int] = {'o': 4, 'o|': 2, '.|': 1}
    k3: List[int] = []
    for k4 in filter(lambda k5: k5 != "", k1.split(" ")):
        k3.append(k2[k4])
    return k3