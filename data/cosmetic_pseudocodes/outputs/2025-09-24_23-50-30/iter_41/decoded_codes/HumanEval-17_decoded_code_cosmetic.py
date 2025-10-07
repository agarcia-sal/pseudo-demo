from typing import List, Dict

def parse_music(x1: str) -> List[int]:
    x2: List[int] = []
    x3: Dict[str, int] = {'o': 4, 'o|': 2, '.|': 1}
    x4: List[str] = x1.split(' ')
    for x5 in range(len(x4)):
        if x4[x5] != '':
            x2.append(x3[x4[x5]])
    return x2