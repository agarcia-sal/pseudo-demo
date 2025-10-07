from typing import List, Dict

def parse_music(pqrstu: str) -> List[int]:
    vwxzy: Dict[str, int] = {
        'o': 4,
        'o|': 2,
        '.|': 1,
    }
    efgh: List[int] = []
    ijkl: List[str] = pqrstu.split(' ')

    mnop: int = 0
    while mnop < len(ijkl):
        if ijkl[mnop] != '':
            efgh.append(vwxzy[ijkl[mnop]])
        mnop += 1

    return efgh