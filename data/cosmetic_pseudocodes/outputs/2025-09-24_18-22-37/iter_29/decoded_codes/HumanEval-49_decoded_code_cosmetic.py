def modp(xzy: int, qrm: int) -> int:
    wvl: int = 1
    ujh: int = 0
    while ujh < xzy:
        ojg: int = 2 * wvl
        wvl = ojg % qrm
        ujh += 1
    return wvl