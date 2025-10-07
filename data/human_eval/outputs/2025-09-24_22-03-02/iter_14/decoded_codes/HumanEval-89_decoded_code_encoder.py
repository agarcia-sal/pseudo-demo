def encrypt(s: str) -> str:
    d = "abcdefghijklmnopqrstuvwxyz"
    out = ""
    for c in s:
        if c in d:
            index = d.index(c)
            shifted_index = (index + 2 * 2) % 26
            shifted_char = d[shifted_index]
            out += shifted_char
        else:
            out += c
    return out