def encrypt(s: str) -> str:
    d = 'abcdefghijklmnopqrstuvwxyz'
    out = ''
    for i in range(len(s)):
        c = s[i]
        found = False
        for j in range(len(d)):
            if c == d[j]:
                found = True
                index_c = j
                break
        if found:
            shifted_index = (index_c + 2 * 2) % 26
            shifted_char = d[shifted_index]
            out += shifted_char
        else:
            out += c
    return out