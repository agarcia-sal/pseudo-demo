def change_base(x: int, base: int) -> str:
    if x <= 0 or base <= 1:
        return ""
    ret = ""
    while x > 0:
        ret = str(x % base) + ret
        x //= base
    return ret