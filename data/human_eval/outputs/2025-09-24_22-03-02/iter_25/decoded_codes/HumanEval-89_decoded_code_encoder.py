def encrypt(s: str) -> str:
    d = 'abcdefghijklmnopqrstuvwxyz'
    out = ''
    i = 0
    while i < len(s):
        c = s[i]
        found_in_d = False
        j = 0
        while j < len(d):
            if d[j] == c:
                found_in_d = True
                break
            j += 1
        if found_in_d:
            new_index = (j + 2 * 2) % 26
            new_char = d[new_index]
            out += new_char
        else:
            out += c
        i += 1
    return out