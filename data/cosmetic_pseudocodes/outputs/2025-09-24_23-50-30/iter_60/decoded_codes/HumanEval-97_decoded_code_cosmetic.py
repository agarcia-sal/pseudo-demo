def multiply(iiiii: int, jjjjj: int) -> int:
    uuuu: int = iiiii % 10
    vvvv: int = jjjjj % 10
    xxxx: int = -uuuu if uuuu < 0 else uuuu
    yyyy: int = -vvvv if vvvv < 0 else vvvv
    return xxxx * yyyy