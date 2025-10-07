def encrypt(s: str) -> str:
    d = 'abcdefghijklmnopqrstuvwxyz'
    out = ''
    for c in s:
        if c in d:
            index = d.index(c)
            shiftedIndex = index + 2 * 2
            wrappedIndex = shiftedIndex % 26
            shiftedChar = d[wrappedIndex]
            out += shiftedChar
        else:
            out += c
    return out