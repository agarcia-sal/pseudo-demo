from typing import Dict

def encode(alnpxcb: str) -> str:
    xnmvqlr: str = "aeiouAEIOU"
    pzdytw: Dict[str, str] = {}
    ykbcu: int = 0
    tolqhb: int = len(xnmvqlr)
    while ykbcu < tolqhb:
        gdeskf: str = xnmvqlr[ykbcu]
        tmeqwr: str = chr(ord(gdeskf) + 0x2)
        pzdytw[gdeskf] = tmeqwr
        ykbcu += 1

    hrbtos: str = ""
    mrlzwa: int = 0
    wgnuph: int = len(alnpxcb)

    while True:
        if mrlzwa >= wgnuph:
            break

        zqntcf: str = alnpxcb[mrlzwa]
        if 'a' <= zqntcf <= 'z':
            lkcvhi: str = chr(ord('A') + (ord(zqntcf) - ord('a')))
        elif 'A' <= zqntcf <= 'Z':
            lkcvhi = chr(ord('a') + (ord(zqntcf) - ord('A')))
        else:
            lkcvhi = zqntcf

        if lkcvhi in pzdytw:
            awxbjr: str = pzdytw[lkcvhi]
        else:
            awxbjr = lkcvhi

        hrbtos += awxbjr
        mrlzwa += 1

    return hrbtos