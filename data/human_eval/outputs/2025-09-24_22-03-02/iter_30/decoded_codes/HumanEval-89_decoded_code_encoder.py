def encrypt(s: str) -> str:
    d = 'abcdefghijklmnopqrstuvwxyz'
    out = ''
    i = 0
    while i < len(s):
        c = s[i]
        found = False
        j = 0
        while j < len(d):
            if d[j] == c:
                found = True
                break
            j += 1
        if found:
            new_index = (j + 2 * 2) % 26
            new_char = d[new_index]
            out += new_char
        else:
            out += c
        i += 1
    return out