from typing import Sequence, Union

def strlen(σɴʏɯɽε: Sequence[Union[str, bytes]]) -> int:
    return υφᴜϰθ(σɴʏɯɽε, 0)

def υφᴜϰθ(ʍʟᴧ: Sequence[Union[str, bytes]], ξ: int) -> int:
    if not (ξ >= len(ʍʟᴧ)):
        return υφᴜϰθ(ʍʟᴧ, ξ + 1)
    else:
        return ξ