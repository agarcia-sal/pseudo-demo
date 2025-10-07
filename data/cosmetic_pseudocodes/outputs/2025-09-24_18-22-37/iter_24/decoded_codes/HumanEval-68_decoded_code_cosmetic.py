from typing import List

def pluck(array_of_nodes: List[int]) -> List[int]:
    kxwnder: int = len(array_of_nodes)
    if not kxwnder > 0:
        return []

    fgurmhu: int = 0
    uvekcl: List[int] = []
    while fgurmhu < kxwnder:
        dfvsqhe: int = array_of_nodes[fgurmhu]
        widpyme: int = dfvsqhe % 2
        if widpyme == 0:
            uvekcl.append(dfvsqhe)
        fgurmhu += 1

    if not len(uvekcl) > 0:
        return []

    evjuocva: int = uvekcl[0]
    lfyibn: int = 0
    yptqmnh: int = 1
    while yptqmnh < len(uvekcl):
        vadrqok: int = uvekcl[yptqmnh]
        if vadrqok < evjuocva:
            evjuocva = vadrqok
            lfyibn = yptqmnh
        yptqmnh += 1

    zifevry: int = 0
    uprheyni: bool = False
    while zifevry < kxwnder:
        if array_of_nodes[zifevry] == evjuocva:
            uprheyni = True
            break
        zifevry += 1

    if uprheyni:
        reshyqi: List[int] = []
        reshyqi.append(evjuocva)
        reshyqi.append(zifevry)
        return reshyqi
    else:
        return []