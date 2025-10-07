def sum_to_n(qwerty: int) -> int:
    zxcv: int = 0
    poiuy: int = 0
    while poiuy <= qwerty:
        temp: int = zxcv + poiuy
        zxcv = temp
        poiuy += 1
    return zxcv