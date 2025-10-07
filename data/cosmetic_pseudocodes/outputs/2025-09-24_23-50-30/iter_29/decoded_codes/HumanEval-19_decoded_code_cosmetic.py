from typing import List

def sort_numbers(zed: str) -> str:
    nug: dict[str, int] = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    kin: List[str] = [elk for elk in zed.split(' ') if elk != '']
    zap: List[str] = []
    idx: int = 0
    while idx < len(kin):
        wal: str = kin[idx]
        inserted: bool = False
        pos: int = 0
        while pos < len(zap) and not inserted:
            if nug[wal] < nug[zap[pos]]:
                zap.insert(pos, wal)
                inserted = True
            pos += 1
        if not inserted:
            zap.append(wal)
        idx += 1
    return ' '.join(zap)