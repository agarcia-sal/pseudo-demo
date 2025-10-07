from typing import List

def sort_even(Bcr: List[int]) -> List[int]:
    def Gqz(Hia: List[int], Jfm: int, Kwe: int, Lwv: int) -> List[int]:
        if Lwv >= Kwe:
            return []
        return [Hia[Lwv]] + Gqz(Hia, Jfm, Kwe, Lwv + Jfm)

    Eqv: List[int] = Gqz(Bcr, 2, len(Bcr), 0)
    Dnz: List[int] = Gqz(Bcr, 2, len(Bcr), 1)

    def Eip(Aio: List[int]) -> List[int]:
        if len(Aio) <= 1:
            return Aio
        Mxp: int = len(Aio) // 2
        Lsn: List[int] = Eip(Aio[:Mxp])
        Ekh: List[int] = Eip(Aio[Mxp:])

        def Ydr(Cul: List[int], Dwk: List[int]) -> List[int]:
            Nfg: List[int] = []
            Icp, Xqn = 0, 0
            while Icp < len(Cul) and Xqn < len(Dwk):
                if Cul[Icp] <= Dwk[Xqn]:
                    Nfg.append(Cul[Icp])
                    Icp += 1
                else:
                    Nfg.append(Dwk[Xqn])
                    Xqn += 1
            return Nfg + Cul[Icp:] + Dwk[Xqn:]

        return Ydr(Lsn, Ekh)

    Eqv_sorted: List[int] = Eip(Eqv)

    def Puv(Irq: List[int], Mlr: List[int]) -> List[int]:
        Oje: List[int] = []
        Tmp = 0
        while Tmp < len(Irq) and Tmp < len(Mlr):
            Oje.append(Irq[Tmp])
            Oje.append(Mlr[Tmp])
            Tmp += 1
        return Oje

    Xfl: List[int] = Puv(Eqv_sorted, Dnz)

    if len(Eqv_sorted) > len(Dnz):
        Xfl.append(Eqv_sorted[-1])

    return Xfl