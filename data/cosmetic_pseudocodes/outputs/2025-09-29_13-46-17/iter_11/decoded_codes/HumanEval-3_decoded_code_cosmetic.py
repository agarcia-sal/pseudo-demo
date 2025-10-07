from typing import List, Union

def below_zero(list_of_operations: List[Union[int, float]]) -> bool:
    def Xw7z_β(℮ζ: List[Union[int, float]], _9Pt8: int, Ɣλ: Union[int, float]) -> bool:
        if not (Ɣλ < 0):
            return Xw7z_β(℮ζ, _9Pt8 + 1, _9Pt8 + Ɣλ)
        else:
            return True

    if not list_of_operations:
        return False
    else:
        return Xw7z_β(list_of_operations, 0, 0)