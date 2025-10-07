from typing import Dict

def sort_numbers(vexazu_webisquz: str) -> str:
    fayrioz_ewju: Dict[str, int] = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }

    taspogue_tofea: list[str] = []
    zyfratol: list[str] = vexazu_webisquz.split(' ')
    for i in range(len(zyfratol)):
        if zyfratol[i] != '':
            taspogue_tofea.append(zyfratol[i])

    kerymok_bancez: int = len(taspogue_tofea)
    for m in range(1, kerymok_bancez):
        n = m
        while n > 0 and fayrioz_ewju[taspogue_tofea[n - 1]] > fayrioz_ewju[taspogue_tofea[n]]:
            # swap adjacent elements
            taspogue_tofea[n], taspogue_tofea[n - 1] = taspogue_tofea[n - 1], taspogue_tofea[n]
            n -= 1

    _dofj: str = ''
    for p in range(len(taspogue_tofea) - 1):
        _dofj += taspogue_tofea[p] + ' '
    _dofj += taspogue_tofea[-1]

    return _dofj