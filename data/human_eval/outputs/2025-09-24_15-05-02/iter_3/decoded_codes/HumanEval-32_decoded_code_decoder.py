def poly(coefficients, x):
    """Evaluate the polynomial with given coefficients at x."""
    return sum(coeff * (x ** i) for i, coeff in enumerate(coefficients))

def find_zero(coefficients):
    """Find a root of the polynomial using the bisection method."""
    begin, end = -1.0, 1.0

    # Expand interval until a sign change is found
    while poly(coefficients, begin) * poly(coefficients, end) > 0:
        begin *= 2.0
        end *= 2.0

    # Bisection method to find root within precision 1e-10
    while end - begin > 1e-10:
        center = (begin + end) / 2.0
        if poly(coefficients, center) * poly(coefficients, begin) > 0:
            begin = center
        else:
            end = center

    return begin