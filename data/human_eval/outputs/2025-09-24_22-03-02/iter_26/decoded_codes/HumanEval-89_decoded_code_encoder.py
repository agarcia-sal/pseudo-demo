def encrypt(s: str) -> str:
    d = 'abcdefghijklmnopqrstuvwxyz'
    out = []
    for c in s:
        if c in d:
            position = d.index(c)
            new_position = (position + 2 * 2) % 26
            out.append(d[new_position])
        else:
            out.append(c)
    return ''.join(out)