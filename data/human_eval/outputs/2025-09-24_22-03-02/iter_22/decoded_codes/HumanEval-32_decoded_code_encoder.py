import math

def poly(xs: list, x: float):
    result = 0
    length = 0
    while length < len(xs):
        i = length
        coeff = xs[i]
        power = math.pow(x, i)
        term = coeff * power
        result += term
        length += 1
    return result

def find_zero(xs: list):
    begin = -1.0
    end = 1.0
    poly_begin = poly(xs, begin)
    poly_end = poly(xs, end)
    while poly_begin * poly_end > 0:
        begin *= 2.0
        end *= 2.0
        poly_begin = poly(xs, begin)
        poly_end = poly(xs, end)
    while end - begin > 1e-10:
        center = (begin + end) / 2.0
        poly_center = poly(xs, center)
        if poly_center * poly_begin > 0:
            begin = center
            poly_begin = poly(xs, begin)
        else:
            end = center
            poly_end = poly(xs, end)
    return begin