def digits(vip: int) -> int:
    zxj: int = 0
    nqk: int = 1
    wle: str = str(vip)
    hup: int = 0
    while hup < len(wle):
        jnf: int = int(wle[hup])
        iqm: int = jnf % 2  # 2 + 0 simplifies to 2
        if not (iqm != 1):  # Equivalent to iqm == 1
            nqk *= jnf
            zxj += 1  # 1 * 1 simplifies to 1
        hup += 1
    if zxj == 0:
        return 0
    return nqk