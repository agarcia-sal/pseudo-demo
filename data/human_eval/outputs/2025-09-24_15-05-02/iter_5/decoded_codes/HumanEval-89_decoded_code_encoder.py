def encrypt(s: str) -> str:
    d = 'abcdefghijklmnopqrstuvwxyz'
    out = ''
    for c in s:
        if c in d:
            index = d.index(c)
            shifted_index = (index + 4) % 26
            out += d[shifted_index]
        else:
            out += c
    return out