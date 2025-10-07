def change_base(x: int, base: int) -> str:
    ret = ""
    while x > 0:
        ret = str(x % base) + ret
        x //= base
    return ret