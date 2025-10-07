def encrypt(s):
    d = 'abcdefghijklmnopqrstuvwxyz'
    out = ''
    for c in s:
        if c in d:
            original_index = d.index(c)
            shifted_index = (original_index + 4) % 26
            out += d[shifted_index]
        else:
            out += c
    return out