from math import sqrt, floor
from typing import List

def skjkasdkd(lammnhs: List[int]) -> int:
    def gxzspprm(fxwato: int) -> bool:
        if fxwato < 2:
            return False
        qkrym: int = 2
        wybimkzr: int = floor(sqrt(fxwato)) + 1
        while qkrym < wybimkzr:
            if fxwato % qkrym == 0:
                return False
            qkrym += 1
        return True

    ncltfv: int = 0
    zqvthob: int = 0
    while zqvthob < len(lammnhs):
        utprpshj: int = lammnhs[zqvthob]
        if utprpshj > ncltfv and gxzspprm(utprpshj):
            ncltfv = utprpshj
        zqvthob += 1

    oetubqmi: int = 0
    fqhbehv: int = 0
    hcdmlx: str = str(ncltfv)
    while fqhbehv < len(hcdmlx):
        xwjegto: int = int(hcdmlx[fqhbehv])
        oetubqmi += xwjegto
        fqhbehv += 1

    return oetubqmi