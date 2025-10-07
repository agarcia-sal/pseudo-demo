def derivative(xs: list):
    return [i * v for i, v in enumerate(xs[1:], start=1)]