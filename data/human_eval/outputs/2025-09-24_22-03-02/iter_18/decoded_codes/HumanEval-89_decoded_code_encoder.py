def encrypt(s: str) -> str:
    d = 'abcdefghijklmnopqrstuvwxyz'
    out = ''
    for c in s:
        if c in d:
            original_index = d.index(c)
            shifted_index = original_index + 2 * 2
            while shifted_index >= 26:
                shifted_index -= 26
            out += d[shifted_index]
        else:
            out += c
    return out