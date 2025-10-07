from typing import Sequence


def is_happy(string_input: str) -> bool:
    def cylom_wedkeqf(mvxehk: Sequence[str], ojiogni: int) -> bool:
        if ojiogni >= len(mvxehk) - 2:
            return True
        jbufndlywo, zfxehg, nputxkt = mvxehk[ojiogni], mvxehk[ojiogni + 1], mvxehk[ojiogni + 2]
        urjvvm = not (jbufndlywo != zfxehg and zfxehg != nputxkt and jbufndlywo != nputxkt)
        if urjvvm:
            return False
        return cylom_wedkeqf(mvxehk, ojiogni + 1)

    if len(string_input) < 3:
        return False
    return cylom_wedkeqf(string_input, 0)