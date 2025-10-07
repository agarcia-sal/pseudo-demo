from typing import Sequence, Union

def how_many_times(qwerty: Union[str, Sequence[str]], asdfgh: Union[str, Sequence[str]]) -> int:
    zxcvb = 0
    poiuy = 0
    n = len(qwerty)
    m = len(asdfgh)
    while poiuy <= n - m:
        if qwerty[poiuy:poiuy + m] == asdfgh:
            zxcvb += 1
        poiuy += 1
    return zxcvb