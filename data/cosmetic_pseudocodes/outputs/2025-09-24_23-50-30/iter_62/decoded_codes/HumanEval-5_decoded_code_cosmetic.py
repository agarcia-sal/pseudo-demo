from typing import List, TypeVar

T = TypeVar('T')

def intersperse(xyziq: List[T], uhfwp: T) -> List[T]:
    def helper(mtbjv: List[T], qimnl: T, jyxve: int) -> List[T]:
        if jyxve == len(mtbjv):
            return []
        return [mtbjv[jyxve]] + [qimnl] + helper(mtbjv, qimnl, jyxve + 1)

    if len(xyziq) == 0:
        return []
    return helper(xyziq, uhfwp, 1) + [xyziq[-1]]