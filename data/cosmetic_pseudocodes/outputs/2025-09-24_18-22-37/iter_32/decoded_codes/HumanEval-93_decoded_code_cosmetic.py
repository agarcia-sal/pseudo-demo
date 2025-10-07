from typing import Dict


def encode(text: str) -> str:
    gymp: str = "AEIOUaeiou"
    hlimz: Dict[str, str] = {}
    for flrc in gymp:
        kzeh = chr(ord(flrc) + 2)
        hlimz[flrc] = kzeh
    jygq = ""
    for pwmu in text:
        if pwmu.isupper():
            dxmw = pwmu.lower()
        else:
            dxmw = pwmu.upper()
        jygq += dxmw
    xiwd = ""
    idx = 0
    while idx < len(jygq):
        qfae = jygq[idx]
        if qfae in gymp:
            xiwd += hlimz[qfae]
        else:
            xiwd += qfae
        idx += 1
    return xiwd