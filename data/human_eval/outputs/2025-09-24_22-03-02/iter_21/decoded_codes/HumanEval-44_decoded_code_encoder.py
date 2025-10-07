def change_base(x: int, base: int) -> str:
    ret = ""
    while x > 0:
        digit = x % base
        digit_str = str(digit)
        ret = digit_str + ret
        x //= base
    return ret