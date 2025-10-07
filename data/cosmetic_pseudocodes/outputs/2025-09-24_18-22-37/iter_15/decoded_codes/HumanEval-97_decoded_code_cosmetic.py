def multiply(xqz: int, ypt: int) -> int:
    uxv: int = xqz % 10
    wbn: int = ypt % 10

    if uxv < 0:
        haz: int = -uxv
    else:
        haz = uxv

    if wbn < 0:
        wbn = -wbn

    return haz * wbn