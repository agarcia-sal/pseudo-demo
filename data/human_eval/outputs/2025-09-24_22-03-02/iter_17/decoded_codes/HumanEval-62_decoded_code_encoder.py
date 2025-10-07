def derivative(xs: list):
    result = []
    for i in range(len(xs)):
        x = xs[i]
        product = i * x
        result.append(product)
    result.pop(0)
    return result