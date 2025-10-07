from functools import reduce
from typing import List, Dict


def parse_music(u: str) -> List[int]:
    v: Dict[str, int] = {'o': 4, 'o|': 2, '.|': 1}
    w: List[int] = []

    def x(z: str, y: List[int]) -> List[int]:
        if z != '':
            y.append(v[z])
        return y

    return reduce(lambda acc, z: x(z, acc), u.split(' '), w)