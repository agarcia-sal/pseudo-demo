def change_base(x: int, base: int) -> str:
    ret = ""
    while x > 0:
        remainder = x % base
        remainder_str = str(remainder)
        ret = remainder_str + ret
        x = x // base
    return ret