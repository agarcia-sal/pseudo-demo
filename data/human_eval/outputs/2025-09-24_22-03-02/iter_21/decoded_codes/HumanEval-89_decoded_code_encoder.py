def encrypt(s: str) -> str:
    d = 'abcdefghijklmnopqrstuvwxyz'
    out = ''
    for c in s:
        if c in d:
            index = d.index(c)
            shifted_index = index + 2 * 2
            wrapped_index = shifted_index % 26
            character = d[wrapped_index]
            out += character
        else:
            out += c
    return out