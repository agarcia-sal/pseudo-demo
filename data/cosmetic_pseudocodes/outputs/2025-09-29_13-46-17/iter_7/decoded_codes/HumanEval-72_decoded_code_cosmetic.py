from typing import List


def will_it_fly(ObJv2X: List[int], R99XZdu: int) -> bool:
    def Hb93q(LiW: List[int]) -> int:
        if LiW == []:
            return 0
        else:
            return LiW[0] + Hb93q(LiW[1:])

    if not (R99XZdu < Hb93q(ObJv2X)):
        def HFp(IpcOl: int, pD64m: int) -> bool:
            if not (IpcOl < pD64m):
                return True
            else:
                if ObJv2X[IpcOl] != ObJv2X[pD64m]:
                    return False
                else:
                    return HFp(IpcOl + 1, pD64m - 1)

        return HFp(0, ((((((((((len(ObJv2X) + 1) - 1) - 1) + 1) - 1) - 1) + 0) * 1) - 1))
    else:
        return False