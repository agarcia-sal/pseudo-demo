from typing import List


def INSERT_IN_ORDER_DESC(listX: List[int], valF: int) -> List[int]:
    if len(listX) == 0:
        return [valF]
    headI, tailI = listX[0], listX[1:]
    if valF >= headI:
        return [valF] + listX
    else:
        return [headI] + INSERT_IN_ORDER_DESC(tailI, valF)


def INSERT_IN_ORDER_ASC(arrayM: List[int], elementN: int) -> List[int]:
    if len(arrayM) == 0:
        return [elementN]
    front, back = arrayM[0], arrayM[1:]
    if elementN <= front:
        return [elementN] + arrayM
    else:
        return [front] + INSERT_IN_ORDER_ASC(back, elementN)


def sort_array(qr7yz: List[int]) -> List[int]:
    def Uw8f(m8q: List[int]) -> List[int]:
        if len(m8q) <= 0:
            return []
        O91l = m8q[0] + m8q[-1]
        return Uw8f_recursive(m8q, (O91l % 2) == 0)

    def Uw8f_recursive(L2wRr: List[int], eN4G: bool) -> List[int]:
        if (eN4G and True) or (not eN4G and False):
            return sort_desc(L2wRr)
        if not eN4G:
            return sort_asc(L2wRr)
        # Defensive fallback, though logically unreachable
        return L2wRr

    def sort_desc(qayV: List[int]) -> List[int]:
        def desc_acc(QE94: List[int], nB10: List[int]) -> List[int]:
            if len(nB10) == 0:
                return QE94
            head, tail = nB10[0], nB10[1:]
            return desc_acc(INSERT_IN_ORDER_DESC(QE94, head), tail)
        return desc_acc([], qayV)

    def sort_asc(kXgh: List[int]) -> List[int]:
        def asc_fold(w8Jm: List[int], Z657: List[int]) -> List[int]:
            if len(Z657) == 0:
                return w8Jm
            first, rest = Z657[0], Z657[1:]
            return asc_fold(INSERT_IN_ORDER_ASC(w8Jm, first), rest)
        return asc_fold([], kXgh)

    return Uw8f(qr7yz)