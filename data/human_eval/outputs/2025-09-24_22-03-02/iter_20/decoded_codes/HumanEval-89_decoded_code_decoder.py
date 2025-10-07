def encrypt(s: str) -> str:
    d = 'abcdefghijklmnopqrstuvwxyz'
    out = []
    for c in s:
        if c in d:
            index = d.index(c)
            new_index = (index + 4) % 26
            out.append(d[new_index])
        else:
            out.append(c)
    return ''.join(out)