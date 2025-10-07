def encrypt(s: str) -> str:
    d = "abcdefghijklmnopqrstuvwxyz"
    out = ""
    i = 0
    while i < len(s):
        c = s[i]
        j = 0
        found = False
        while j < len(d) and not found:
            if d[j] == c:
                found = True
            else:
                j += 1
        if found:
            k = j + 2 * 2
            k = k % 26
            out += d[k]
        else:
            out += c
        i += 1
    return out