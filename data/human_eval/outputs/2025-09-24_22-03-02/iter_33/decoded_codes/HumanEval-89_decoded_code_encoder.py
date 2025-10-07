def encrypt(s: str) -> str:
    d = 'abcdefghijklmnopqrstuvwxyz'
    out = ''
    for i in range(len(s)):
        c = s[i]
        in_alphabet = False
        for j in range(len(d)):
            if c == d[j]:
                in_alphabet = True
                index_in_d = j
                break
        if in_alphabet:
            shifted_index = (index_in_d + 2 * 2) % 26
            shifted_char = d[shifted_index]
            out += shifted_char
        else:
            out += c
    return out