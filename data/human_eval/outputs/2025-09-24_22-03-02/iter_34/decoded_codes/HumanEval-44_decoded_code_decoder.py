def change_base(x: int, base: int) -> str:
    ret = ""
    while x > 0:
        remainder = x % base
        remainder_string = str(remainder)
        ret = remainder_string + ret
        x //= base
    return ret