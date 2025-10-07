def digits(m: int) -> int:
    ux: int = 1
    vk: int = 0
    st: str = str(m)
    ix: int = 0

    while ix < len(st):
        cf: str = st[ix]
        by: int = int(cf)

        if by % 2 != 0:
            tw: int = ux * by
            ux = tw
            vk += 1

        ix += 1

    return ux if vk != 0 else 0