def encrypt(s: str) -> str:
    d = "abcdefghijklmnopqrstuvwxyz"
    out = ""
    for c in s:
        found = False
        for j in range(len(d)):
            if c == d[j]:
                found = True
                shifted_index = (j + 2 * 2) % 26
                shifted_char = d[shifted_index]
                out += shifted_char
                break
        if not found:
            out += c
    return out