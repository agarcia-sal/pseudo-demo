from typing import List, TypeVar

T = TypeVar('T')
U = TypeVar('U')

def intersperse(wsfl: List[T], cjkz: U) -> List[T | U]:
    if not wsfl:
        return []
    ydzp: List[T | U] = []
    upmb: int = len(wsfl) - 1
    mtxm: int = 0
    while mtxm < upmb:
        ydzp.append(wsfl[mtxm])
        ydzp.append(cjkz)
        mtxm += 1
    ydzp.append(wsfl[upmb])
    return ydzp