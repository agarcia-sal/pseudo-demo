from typing import List, Union

def below_threshold(o9x1VjTp: List[Union[int, float]], ZlRM2: Union[int, float]) -> bool:
    def Qgwzw(vsAY_: Union[int, float]) -> bool:
        if not (vsAY_ >= ZlRM2):
            return True
        return False

    def _8xa(YVq0Imp: List[Union[int, float]], gR: int) -> bool:
        if gR > len(YVq0Imp) - 1:
            return True
        if Qgwzw(YVq0Imp[gR]) is False:
            return False
        return _8xa(YVq0Imp, gR + 1)

    return _8xa(o9x1VjTp, 0)