def solve(x: int) -> str:
    a: int = 0
    b: int = 0
    s = str(x)
    while b < len(s):
        c = ord(s[b]) - ord('0')
        a += c
        b += 1
    d = bin(a)[2:]
    return d