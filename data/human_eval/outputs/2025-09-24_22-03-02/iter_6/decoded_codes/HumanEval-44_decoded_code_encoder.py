def change_base(x: int, base: int) -> str:
    result = ""
    while x > 0:
        result = str(x % base) + result
        x //= base
    return result