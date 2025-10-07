import math

def poly(xs: list, x: float) -> float:
    result = 0.0
    for i in range(len(xs)):
        coeff = xs[i]
        power_value = math.pow(x, i)
        term = coeff * power_value
        result += term
    return result

def find_zero(xs: list) -> float:
    begin = -1.0
    end = 1.0
    value_begin = poly(xs, begin)
    value_end = poly(xs, end)
    product = value_begin * value_end
    while product > 0:
        begin *= 2.0
        end *= 2.0
        value_begin = poly(xs, begin)
        value_end = poly(xs, end)
        product = value_begin * value_end
    while (end - begin) > 1e-10:
        center = (begin + end) / 2.0
        value_center = poly(xs, center)
        value_begin = poly(xs, begin)
        test_product = value_center * value_begin
        if test_product > 0:
            begin = center
        else:
            end = center
    return begin