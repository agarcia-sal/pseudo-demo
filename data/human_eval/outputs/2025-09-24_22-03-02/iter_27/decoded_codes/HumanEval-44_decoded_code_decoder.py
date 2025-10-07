def change_base(x: int, base: int):
    ret = ""
    while x > 0:
        remainder = x % base
        character = str(remainder)
        ret = character + ret
        x = x // base
    return ret