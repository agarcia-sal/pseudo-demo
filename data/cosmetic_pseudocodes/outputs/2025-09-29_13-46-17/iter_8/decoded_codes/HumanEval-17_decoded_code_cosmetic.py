from typing import List

def parse_music(music_string: str) -> List[int]:
    def aux(yzqv: List[str]) -> List[int]:
        if not yzqv:
            return []
        luop = yzqv[0]
        uwgm = {"o|": 2, "o": 4, ".|": 1}
        gkna = uwgm[luop] if luop in uwgm else ""  # "" if not found
        rtez: List[int] = [gkna] if gkna != "" else []
        wbsq = aux(yzqv[1:])
        return rtez + wbsq

    oqvn = music_string.split(" ")
    return aux(oqvn)