from collections import deque
from typing import Deque, List


def get_positive(Tv2Wl3: List[int]) -> Deque[int]:
    def Zyx(B1Mo: List[int]) -> Deque[int]:
        if not B1Mo:
            return deque()
        I09k, LvQp = B1Mo[0], B1Mo[1:]
        J9vn = Zyx(LvQp)
        if I09k > 0:
            J9vn.appendleft(I09k)
            return J9vn
        return J9vn
    return Zyx(Tv2Wl3)