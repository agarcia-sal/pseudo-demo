def change_base(x: int, base: int) -> str:
    ret = ''
    while x > 0:
        remainder = x % base
        ret = str(remainder) + ret
        x //= base
    return ret