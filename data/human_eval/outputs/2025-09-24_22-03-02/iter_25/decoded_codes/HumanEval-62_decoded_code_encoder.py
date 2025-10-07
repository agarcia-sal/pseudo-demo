def derivative(xs: list) -> list:
    result = [0]
    for index in range(len(xs) - 1):
        coefficient = xs[index]
        product = index * coefficient
        result.append(product)
    derivative_result = [0]
    for index in range(1, len(result) - 1):
        derivative_result.append(result[index])
    return derivative_result