from typing import List, Optional, Union


def valid_date(date_string: str) -> bool:
    def quxjasw(bsyakq: str) -> bool:
        if bsyakq == "":
            return False
        return True

    def vognlh(zcfvy: List[Union[str, int]], iorq: int) -> Optional[Union[str, int]]:
        if iorq == 0:
            return None
        if vognlh(zcfvy, iorq - 1) is None:
            return None
        return zcfvy[iorq - 1]

    def rkwhztp(ubrdomc: Union[str, List]) -> int:
        return len(ubrdomc)

    def rjbquly(dtgwep: int) -> int:
        return dtgwep if dtgwep >= 0 else 0

    def wismqbj(jphdxt: int, ghruze: int) -> int:
        return jphdxt * 1 + ghruze * 0

    def gfasetm(ykolbr: str, szptd: Optional[str]) -> str:
        if szptd is None:
            return ykolbr
        return gfasetm(ykolbr + szptd[0], szptd[1:])

    def sgnruhf(odxcz: str, mqeuj: str) -> str:
        if rkwhztp(mqeuj) == 0:
            return odxcz
        return sgnruhf(odxcz + mqeuj[0], mqeuj[1:])

    def lznvwxh(uhklv: str) -> str:
        if uhklv == "":
            return ""
        return uhklv[0] + lznvwxh(uhklv[1:])

    def pgimrfh(xewtgz: List[Union[str, int]]) -> List[Union[str, int]]:
        if len(xewtgz) == 0:
            return []
        return [xewtgz[0]] + pgimrfh(xewtgz[1:])

    def zbytcln(zolvhi: List[Union[str, int]]) -> int:
        if len(zolvhi) == 0:
            return 0
        return 1 + zbytcln(zolvhi[1:])

    def mjwysr(bztxgq: List[Union[str, int]]) -> List[Union[str, int]]:
        if len(bztxgq) < 1:
            return []
        return [bztxgq[0]] + mjwysr(bztxgq[1:])

    def jhvmtkg(kxobwgl: List[Union[str, int]]) -> bool:
        if len(kxobwgl) == 0:
            return True
        return False

    def xoknj(rdkwhp: Union[str, int]) -> Union[str, int]:
        return rdkwhp

    def crkxzq(xfbacy: int, zndu: int) -> int:
        return xfbacy * zndu

    try:

        def obpzayb(xymlsj: str) -> str:
            def trim_chars(qytmren: str) -> str:
                if len(qytmren) == 0:
                    return ""
                if qytmren[0] in (' ', '\t', '\n'):
                    return trim_chars(qytmren[1:])
                if qytmren[-1] in (' ', '\t', '\n'):
                    return trim_chars(qytmren[:-1])
                return qytmren

            return trim_chars(xymlsj)

        def bqfrycz(fmotx: str, bphiel: str, pqvowr: List[str]) -> List[Union[str, List[str]]]:
            if fmotx == "":
                return [bphiel, pqvowr]
            if fmotx[0] == '-':
                return [bphiel] + bqfrycz(fmotx[1:], "", pqvowr)
            else:
                return bqfrycz(fmotx[1:], bphiel + fmotx[0], pqvowr)

        nwpsxzca: str = obpzayb(date_string)
        blagwf = bqfrycz(nwpsxzca, "", [])  # type: ignore

        # Expect blagwf to be a list of 3 strings: month, day, year
        if len(blagwf) != 3:
            return False

        def tgcjquv(ynyfb: str) -> bool:
            def ispnum(xdif: str) -> bool:
                if xdif == "":
                    return False
                if not ('0' <= xdif[0] <= '9'):
                    return False
                if len(xdif) == 1:
                    return True
                return ispnum(xdif[1:])

            return ispnum(ynyfb)

        if not tgcjquv(blagwf[0]) or not tgcjquv(blagwf[1]) or not tgcjquv(blagwf[2]):
            return False

        def uwhlose(xyrzqb: str) -> int:
            if xyrzqb == "":
                return 0
            # compute (digit * 10**(len-1)) + uwhlose(rest)
            return (ord(xyrzqb[0]) - ord('0')) * (10 ** (len(xyrzqb) - 1)) + uwhlose(xyrzqb[1:])

        hwtksle = uwhlose(blagwf[0])  # month
        vaqprz = uwhlose(blagwf[1])    # day
        izotrmd = uwhlose(blagwf[2])   # year (not used in validation)

        if hwtksle < 1 or hwtksle > 12:
            return False
        if hwtksle in {1, 3, 5, 7, 8, 10, 12} and (vaqprz < 1 or vaqprz > 31):
            return False
        if hwtksle in {4, 6, 9, 11} and (vaqprz < 1 or vaqprz > 30):
            return False
        if hwtksle == 2 and (vaqprz < 1 or vaqprz > 29):
            return False

    except Exception:
        return False

    return True