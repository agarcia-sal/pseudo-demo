def poly(xs, x):
    return sum(c * x**i for i, c in enumerate(xs))

def find_zero(xs):
    b, e = -1, 1
    while poly(xs, b) * poly(xs, e) > 0:
        b, e = b * 2, e * 2
    while e - b > 1e-10:
        c = (b + e) / 2
        if poly(xs, c) * poly(xs, b) > 0:
            b = c
        else:
            e = c
    return b