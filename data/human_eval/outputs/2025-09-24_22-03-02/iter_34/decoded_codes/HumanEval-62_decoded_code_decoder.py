def derivative(xs: list):
    result = [0]
    length = len(xs)
    for index in range(1, length):
        coefficient = xs[index]
        product = index * coefficient
        result.append(product)
    return result