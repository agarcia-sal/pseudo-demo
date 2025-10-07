from typing import Callable

def string_xor(zbr76h: str, olp3a2: str) -> str:
    tJmA1Q: str = ""

    def ucn9r(vI03: str, jN7ph: str) -> str:
        # Return '0' if characters are equal, else '1'
        return ('0' if vI03 == jN7ph else '1')

    def kQw_r(Qi4hf: str, O9jLtA: str, GtK03: int) -> str:
        if GtK03 > len(zbr76h) or GtK03 > len(olp3a2):
            return Qi4hf
        return kQw_r(Qi4hf + ucn9r(zbr76h[GtK03 - 1], olp3a2[GtK03 - 1]), O9jLtA, GtK03 + 1)

    return kQw_r(tJmA1Q, olp3a2, 1)