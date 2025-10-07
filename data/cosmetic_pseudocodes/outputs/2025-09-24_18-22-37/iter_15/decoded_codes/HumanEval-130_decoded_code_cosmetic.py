from typing import List


def tri(integer_n: int) -> List[int]:
    if integer_n == 0:
        return [1]

    wxo: List[int] = [1, 3]
    yvb: int = 2

    while yvb <= integer_n:
        puq: int = yvb % 2
        if puq == 0:
            gmr: int = (yvb // 2) + 1
            wxo.append(gmr)
        else:
            gmr = wxo[yvb - 1] + wxo[yvb - 2]
            puq = (yvb + 3) // 2
            gmr += puq
            wxo.append(gmr)
        yvb += 1

    return wxo