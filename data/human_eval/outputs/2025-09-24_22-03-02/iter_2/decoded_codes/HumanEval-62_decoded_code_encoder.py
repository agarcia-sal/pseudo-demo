def derivative(xs):
    return [index * coefficient for index, coefficient in enumerate(xs[1:], start=1)]