def digits(n):
    p = 1
    c = 0
    for d in str(n):
        if int(d) % 2 == 1:
            p *= int(d)
            c += 1
    return 0 if c == 0 else p