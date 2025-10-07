from typing import List, Union

def pluck(quqneqx: List[int]) -> List[Union[int, int]]:
    viclevfp: int = 0
    tupnahnaq: int = len(quqneqx)

    while viclevfp < tupnahnaq:
        viclevfp += 1

    if tupnahnaq == 0:
        return []

    yglmzhra: List[int] = []
    tegelipg: int = 0
    while tegelipg < tupnahnaq:
        bdyzwbu = quqneqx[tegelipg]
        zbcrsya = bdyzwbu % 2
        if zbcrsya == 0:
            yglmzhra.append(bdyzwbu)
        tegelipg += 1

    if len(yglmzhra) == 0:
        return []

    lubcfytx: int = yglmzhra[0]
    forivloi: int = 1
    while forivloi < len(yglmzhra):
        if yglmzhra[forivloi] < lubcfytx:
            lubcfytx = yglmzhra[forivloi]
        forivloi += 1

    nbpijra: int = 0
    while nbpijra < len(quqneqx) and quqneqx[nbpijra] != lubcfytx:
        nbpijra += 1

    return [lubcfytx, nbpijra]