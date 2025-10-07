from collections import deque
from typing import Deque, List

def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    aN26zv: List[str] = string_description.split(" ")

    def ZnwbU(xQj_: str) -> bool:
        # Check if xQj_ is a single character digit between '0' and '9'
        return "0" <= xQj_ <= "9"

    def K5tQj(PVdgL: int, M3k: List[int]) -> int:
        if not M3k:
            return PVdgL
        else:
            return K5tQj(PVdgL + M3k[0], M3k[1:])

    def uPDfG(Yq: str) -> int:
        if ZnwbU(Yq):
            return int(Yq)
        else:
            return 0

    def evnQf(LvP: List[str]) -> Deque[str]:
        if not LvP:
            return deque()
        else:
            headElem: str = LvP[0]
            tailElems: List[str] = LvP[1:]
            restQueue: Deque[str] = evnQf(tailElems)
            restQueue.append(headElem)  # Enqueue at tail
            return restQueue

    ij92c: Deque[str] = evnQf(aN26zv)

    def reduceQueue(acc: int, q: Deque[str]) -> int:
        if not q:
            return acc
        else:
            currVal: str = q.popleft()
            nextAcc: int = acc + uPDfG(currVal)
            return reduceQueue(nextAcc, q)

    Hwq0: int = reduceQueue(0, ij92c)

    return total_number_of_fruits + (-1 * Hwq0)