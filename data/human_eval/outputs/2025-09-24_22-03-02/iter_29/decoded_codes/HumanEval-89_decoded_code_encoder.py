def encrypt(s: str) -> str:
    d = 'abcdefghijklmnopqrstuvwxyz'
    out = ''
    for c in s:
        found = False
        for j, ch in enumerate(d):
            if c == ch:
                found = True
                new_index = (j + 2 * 2) % 26
                out += d[new_index]
                break
        if not found:
            out += c
    return out