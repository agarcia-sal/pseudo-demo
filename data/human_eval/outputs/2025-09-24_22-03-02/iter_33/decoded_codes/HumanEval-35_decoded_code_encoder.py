def max_element(l: list) -> int:
    m = l[0]
    i = 0
    while i < len(l):
        e = l[i]
        if e > m:
            m = e
        i += 1
    return m