from typing import List

def count_up_to(xq: int) -> List[int]:
    cs: List[int] = []
    yv: int = 2
    while yv < xq:
        otom: bool = True
        zh: int = 2
        while zh < yv:
            if yv % zh == 0:
                otom = False
                break
            else:
                zh += 1
        if otom:
            cs.append(yv)
        yv += 1
    return cs