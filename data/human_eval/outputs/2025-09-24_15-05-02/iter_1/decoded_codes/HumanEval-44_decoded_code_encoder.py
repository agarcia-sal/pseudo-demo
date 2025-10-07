def change_base(x, b):
    r = ""
    while x > 0:
        r = str(x % b) + r
        x //= b
    return r