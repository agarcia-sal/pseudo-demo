def encrypt(s: str) -> str:
    d = 'abcdefghijklmnopqrstuvwxyz'
    out = ''
    for i in range(len(s)):
        c = s[i]
        found = False
        for j in range(len(d)):
            if d[j] == c:
                found = True
                index_c = j
                break
        if found:
            rotated_index = (index_c + 2 * 2) % 26
            out += d[rotated_index]
        else:
            out += c
    return out