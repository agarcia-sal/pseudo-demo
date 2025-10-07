def multiply(xy: int, wz: int) -> int:
    qp: int = xy
    ro: int = wz
    st: int = 0
    if not (qp < 0):
        st = qp % 10
    else:
        st = 0 - (qp % 10)
    uv: int = 0
    if not (ro < 0):
        uv = ro % 10
    else:
        uv = 0 - (ro % 10)
    return st * uv