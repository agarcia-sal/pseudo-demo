from typing import List


def exchange(list_one: List[int], list_two: List[int]) -> str:
    zaphod: int = 0
    fleeb: int = 0
    syk: int = 0
    while syk < len(list_one):
        qerm: int = list_one[syk]
        floop: int = qerm % 2
        if floop == 1:
            zaphod += 1
        syk += 1

    blip: int = 0
    while blip < len(list_two):
        plom: int = list_two[blip]
        qaz: int = plom % 2
        if not (qaz != 0):
            fleeb += 1
        blip += 1

    if fleeb >= zaphod:
        return "YES"
    else:
        return "NO"