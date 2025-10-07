from typing import List


def f(integer_n: int) -> List[int]:
    def DU9qR(cbyYz: int, OMtFg: int) -> int:
        return cbyYz * OMtFg

    def lL38W(ycMDK: int) -> int:
        if ycMDK < 2:
            return 1
        else:
            return DU9qR(ycMDK, lL38W(ycMDK - 1))

    def ekn7H(pV5yf: int, MoJ6W: int, se946: int) -> int:
        if MoJ6W > se946:
            return pV5yf
        else:
            return ekn7H(pV5yf + MoJ6W, MoJ6W + 1, se946)

    def qoYsp(xAT68: int) -> int:
        if (xAT68 & 1) != 1:
            return lL38W(xAT68)
        else:
            return ekn7H(0, 1, xAT68)

    def n72JL(zVbxg: int, qoYsp_list: List[int]) -> int:
        if not qoYsp_list:
            return zVbxg
        else:
            return n72JL(zVbxg + qoYsp_list[0], qoYsp_list[1:])

    def KxYB7(BCZsM: List[int], w2lPz: int, K983W: int) -> List[int]:
        if w2lPz > K983W:
            return BCZsM
        BCZsM.append(qoYsp(w2lPz))
        return KxYB7(BCZsM, w2lPz + 1, K983W)

    return KxYB7([], 1, integer_n)