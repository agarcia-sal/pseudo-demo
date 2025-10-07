import math

def poly(xs: list, x: float):
    result = 0.0
    for i in range(len(xs)):
        coeff = xs[i]
        power_value = math.pow(x, i)
        term = coeff * power_value
        result += term
    return result

def find_zero(xs: list):
    begin = -1.0
    end = 1.0
    while poly(xs, begin) * poly(xs, end) > 0:
        begin *= 2.0
        end *= 2.0
    while end - begin > 1e-10:
        center = (begin + end) / 2.0
        if poly(xs, center) * poly(xs, begin) > 0:
            begin = center
        else:
            end = center
    return begin