def flip_case(x: str) -> str:
    y = []
    i = 0
    while i < len(x):
        c = x[i]
        if 'a' <= c <= 'z':
            y.append(c.upper())
        elif 'A' <= c <= 'Z':
            y.append(c.lower())
        else:
            y.append(c)
        i += 1
    return ''.join(y)