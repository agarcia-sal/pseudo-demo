import math

def poly(xs: list, x: float):
    total = 0
    for i, coeff in enumerate(xs):
        power_result = math.pow(x, i)
        product = coeff * power_result
        total += product
    return total

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