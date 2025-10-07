def encrypt(s: str) -> str:
    d = "abcdefghijklmnopqrstuvwxyz"
    out = ""
    for i in range(len(s)):
        c = s[i]
        found = False
        for j in range(len(d)):
            if c == d[j]:
                found = True
                break
        if found == True:
            index_c = 0
            for k in range(len(d)):
                if c == d[k]:
                    index_c = k
                    break
            new_index = (index_c + 2 * 2) % 26
            out += d[new_index]
        else:
            out += c
    return out