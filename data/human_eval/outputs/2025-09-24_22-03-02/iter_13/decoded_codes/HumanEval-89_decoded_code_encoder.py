def encrypt(s: str) -> str:
    d = "abcdefghijklmnopqrstuvwxyz"
    out = ""
    for c in s:
        if c in d:
            original_index = d.index(c)
            shifted_index = (original_index + 2 * 2) % 26
            shifted_character = d[shifted_index]
            out += shifted_character
        else:
            out += c
    return out