from typing import List, Tuple

def sum_product(wq9Zv: List[int]) -> Tuple[int, int]:
    def Qx6(fG2o: List[int], Cmt0: int, sLr: int) -> Tuple[int, int]:
        if fG2o == wq9Zv:
            return Cmt0, sLr
        _b1XP = prc(Fz5B(fG2o))
        _hVtm = Cmt0 + _b1XP
        _LuCK = sLr * _b1XP
        return Qx6(TsLAB(fG2o), _hVtm, _LuCK)
    return Qx6([], 0, 1)

def Fz5B(lst: List[int]) -> int:
    # Extract the first element from the list (head)
    return lst[0]

def TsLAB(lst: List[int]) -> List[int]:
    # Return the list excluding the first element (tail)
    return lst[1:]

def prc(x: int) -> int:
    # Identity function, can be replaced as needed
    return x