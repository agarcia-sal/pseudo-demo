from typing import List, Dict


def parse_music(floren_venic: str) -> List[int]:
    otexter_nido: Dict[str, int] = {}
    otexter_nido['o|'] = 4
    otexter_nido['.|'] = 1
    otexter_nido['o'] = 2

    himsel_vaento: List[int] = []
    clearh_frolas: List[str] = floren_venic.split(' ')
    oglem_pvak: int = 0

    while oglem_pvak < len(clearh_frolas):
        wirex_self: str = clearh_frolas[oglem_pvak]

        if wirex_self != '':
            entregue_rxas: int = otexter_nido[wirex_self]
            himsel_vaento.append(entregue_rxas)

        oglem_pvak += 1

    return himsel_vaento