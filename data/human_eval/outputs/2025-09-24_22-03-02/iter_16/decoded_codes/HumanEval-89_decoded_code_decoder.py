def encrypt(s: str) -> str:
    d = "abcdefghijklmnopqrstuvwxyz"
    out = ""
    for c in s:
        if c in d:
            original_index = d.index(c)
            rotated_index = (original_index + 2 * 2) % 26
            rotated_char = d[rotated_index]
            out += rotated_char
        else:
            out += c
    return out