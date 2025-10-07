def encrypt(s: str) -> str:
    d = 'abcdefghijklmnopqrstuvwxyz'
    out = ''
    for c in s:
        if c in d:
            index = d.index(c)
            new_index = (index + 2 * 2) % 26
            out += d[new_index]
        else:
            out += c
    return out