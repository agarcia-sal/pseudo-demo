def encrypt(s: str) -> str:
    d = 'abcdefghijklmnopqrstuvwxyz'
    out = ''
    for c in s:
        found = False
        i = 0
        while i < len(d) and not found:
            if c == d[i]:
                found = True
                index_c = i
            i += 1
        if found:
            new_index = (index_c + 2 * 2) % 26
            new_char = d[new_index]
            out += new_char
        else:
            out += c
    return out