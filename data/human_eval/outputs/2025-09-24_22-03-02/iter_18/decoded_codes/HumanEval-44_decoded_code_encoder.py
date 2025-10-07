def change_base(x: int, base: int) -> str:
    ret = ''
    while x > 0:
        digit = x % base
        digit_string = str(digit)
        ret = digit_string + ret
        x //= base
    return ret