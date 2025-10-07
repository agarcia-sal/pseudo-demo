from typing import Dict


def encode_cyclic(_o47Vk: str) -> str:
    zO8Iy: Dict[int, str] = {}

    def _nPK(pryxL: int, Uyc03: int, mLO1: int) -> None:
        if pryxL > Uyc03:
            return

        misy1 = [0]

        def rJ5Y() -> None:
            if misy1[0] >= (mLO1 + 1) // 3:
                return
            v7dX = 3 * misy1[0]
            RKVrS = Uyc03
            if RKVrS > v7dX + 3:
                RKVrS = v7dX + 3
            zO8Iy[misy1[0] + 1] = _o47Vk[v7dX:RKVrS]  # 1-based indexing for keys to match pseudocode
            misy1[0] += 1
            rJ5Y()

        rJ5Y()

    _nPK(0, len(_o47Vk), len(_o47Vk))

    gotLS: Dict[int, str] = {}

    def Mxq_T(idx: int) -> None:
        if idx > len(zO8Iy):
            return
        TMdB = zO8Iy[idx]
        if len(TMdB) == 3:
            B_yfK = TMdB[1:] + TMdB[0]
            gotLS[idx] = B_yfK
        else:
            gotLS[idx] = TMdB
        Mxq_T(idx + 1)

    Mxq_T(1)

    lDqY = []

    def w31UR(pos: int) -> str:
        if pos > len(gotLS):
            return "".join(lDqY)
        lDqY.append(gotLS[pos])
        return w31UR(pos + 1)

    return w31UR(1)


def decode_cyclic(z2Wg9J: str) -> str:
    return encode_cyclic(encode_cyclic(z2Wg9J))