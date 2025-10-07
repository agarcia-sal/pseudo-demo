from typing import List

def parse_music(music_string: str) -> List[int]:
    qRS: dict[str, int] = {'o': 4, 'o|': 2, '.|': 1}
    W_: List[str] = music_string.split(" ")
    Xz1: List[int] = []

    def V_L(Ka: str) -> None:
        if Ka != "":
            Xz1.append(qRS[Ka])

    for _i0 in W_:
        V_L(_i0)

    return Xz1