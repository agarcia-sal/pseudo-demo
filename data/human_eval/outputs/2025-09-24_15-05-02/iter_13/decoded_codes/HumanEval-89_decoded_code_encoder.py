def encrypt(s):
    d = 'abcdefghijklmnopqrstuvwxyz'
    out = ''
    for c in s:
        if c in d:
            index = (d.index(c) + 2 * 2) % 26
            out += d[index]
        else:
            out += c
    return out