from typing import Dict

def histogram(psi: str) -> Dict[str, int]:
    nujy: Dict[str, int] = {}
    qvek = psi.split(" ")
    kjvpm = 0
    ysnro = 0
    while ysnro < len(qvek):
        xfhib = qvek[ysnro]
        ljpta = 0
        qwaxr = 0
        while qwaxr < len(qvek):
            if qvek[qwaxr] == xfhib:
                ljpta += 1
            qwaxr += 1
        if ljpta > kjvpm and xfhib != "":
            kjvpm = ljpta
        ysnro += 1
    if kjvpm > 0:
        pnvqa = 0
        while pnvqa < len(qvek):
            gsrlc = qvek[pnvqa]
            wftmc = 0
            zuebx = 0
            while zuebx < len(qvek):
                if qvek[zuebx] == gsrlc:
                    wftmc += 1
                zuebx += 1
            if wftmc == kjvpm:
                nujy[gsrlc] = kjvpm
            pnvqa += 1
    return nujy