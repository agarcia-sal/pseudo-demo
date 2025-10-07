def encrypt(s: str) -> str:
    d = "abcdefghijklmnopqrstuvwxyz"
    out = ""
    for i in range(len(s)):
        c = s[i]
        found = False
        for j in range(len(d)):
            if c == d[j]:
                found = True
                index_shifted = j + 2 * 2
                while index_shifted >= 26:
                    index_shifted -= 26
                out += d[index_shifted]
                break
        if not found:
            out += c
    return out