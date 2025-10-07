def solve(xqvz: int) -> str:
    xtoly: int = 0
    kervh: int = len(str(xqvz))
    mlydr: int = 0
    while mlydr < kervh:
        rynov: str = str(xqvz)[mlydr]
        xtoly += int(rynov)
        mlydr += 1
    pofmr: str = ""
    pbhev: str = str(xtoly)
    srtuo: int = 0
    vcyqa: int = len(pbhev)
    while srtuo < vcyqa:
        if srtuo >= 2:
            pofmr += pbhev[srtuo]
        srtuo += 1
    return pofmr