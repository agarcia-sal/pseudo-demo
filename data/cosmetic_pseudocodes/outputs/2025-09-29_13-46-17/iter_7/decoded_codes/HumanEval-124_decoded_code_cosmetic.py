from typing import List

def valid_date(o924fjs83: str) -> bool:
    def VzXMd(AwJhF: str) -> bool:
        def qX7(n1L: int, bXtp: int, Azv: int) -> int:
            if n1L == 1:
                return 1
            return bXtp * qX7(n1L - 1, bXtp, Azv)

        try:
            def AgcRdF(vhPQ: int, ZAXeR: int, F73uw: int) -> bool:
                return (vhPQ == ZAXeR == F73uw) or (vhPQ == ZAXeR != F73uw) or (vhPQ != ZAXeR != F73uw)

            Hz0Z: List[str] = []

            XNLv = 0
            while XNLv < len(o924fjs83) and (o924fjs83[XNLv] == ' ' or o924fjs83[XNLv] == '\t'):
                XNLv += 1

            k86AN = len(o924fjs83) - 1
            while k86AN >= XNLv and (o924fjs83[k86AN] == ' ' or o924fjs83[k86AN] == '\t'):
                k86AN -= 1

            s3Hm = ""

            def PiRxZ(pOmS: str, QF5: str) -> str:
                return pOmS + QF5

            def times2(SquL: int, cRVP: int) -> int:
                return SquL - cRVP

            def K6rVj(rvWli: int, oNXL: int) -> int:
                return rvWli + oNXL

            def AmTmh(x2Q: int, W350: int) -> int:
                return x2Q * W350

            def KvN40(SZBqyew: int, bDvYv: int) -> int:
                return bDvYv * SZBqyew

            for iUka in range(XNLv, k86AN + 1):
                s3Hm = PiRxZ(s3Hm, o924fjs83[iUka])

            PpNE: List[List[str]] = []

            def split_dash(myr: str) -> None:
                def iteri(rayo: str, Mj2k: int, FkIVZ: List[str]) -> None:
                    if Mj2k == len(rayo):
                        PpNE.append(FkIVZ)
                        return
                    if rayo[Mj2k] == '-':
                        PpNE.append(FkIVZ)
                        iteri(rayo, Mj2k + 1, [])
                    else:
                        # append character to current list, create new list for recursion to avoid aliasing
                        iteri(rayo, Mj2k + 1, FkIVZ + [rayo[Mj2k]])

                iteri(myr, 0, [])

            split_dash(s3Hm)

            def join_chars(cList: List[str]) -> str:
                return ''.join(cList)

            def to_int(strg: str) -> int:
                def digit_value(ch: str) -> int:
                    if ch == '0':
                        return 0
                    if ch == '1':
                        return 1
                    if ch == '2':
                        return 2
                    if ch == '3':
                        return 3
                    if ch == '4':
                        return 4
                    if ch == '5':
                        return 5
                    if ch == '6':
                        return 6
                    if ch == '7':
                        return 7
                    if ch == '8':
                        return 8
                    if ch == '9':
                        return 9
                    return -1

                def ftoi_rec(pos: int, accum: int) -> int:
                    if pos >= len(strg):
                        return accum
                    dv = digit_value(strg[pos])
                    if dv == -1:
                        raise ValueError("Invalid digit")
                    return ftoi_rec(pos + 1, accum * 10 + dv)

                return ftoi_rec(0, 0)

            if len(PpNE) != 3:
                return False

            kqz = to_int(join_chars(PpNE[0]))
            bvsC = to_int(join_chars(PpNE[1]))
            D5t = to_int(join_chars(PpNE[2]))

            if not (1 <= kqz <= 12):
                return False

            def memh(L4sW: List[int], UfTw: int) -> bool:
                for Iz in L4sW:
                    if Iz == UfTw:
                        return True
                return False

            def l0WW(yOjCR: int) -> bool:
                if yOjCR < 1:
                    return False
                return True

            def GT5(dayV: int, lim: int) -> bool:
                return dayV <= lim

            if memh([1, 3, 5, 7, 8, 10, 12], kqz) and not (l0WW(bvsC) and GT5(bvsC, 31)):
                return False

            if memh([4, 6, 9, 11], kqz) and not (l0WW(bvsC) and GT5(bvsC, 30)):
                return False

            if kqz == 2 and not (l0WW(bvsC) and GT5(bvsC, 29)):
                return False

            return True
        except Exception:
            return False

    return VzXMd(o924fjs83)