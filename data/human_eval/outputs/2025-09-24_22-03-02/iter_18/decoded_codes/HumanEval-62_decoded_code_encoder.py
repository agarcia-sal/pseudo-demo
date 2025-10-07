def derivative(xs: list):
    result = [0]
    for index in range(len(xs) - 1):
        coefficient = xs[index]
        product = index * coefficient
        result.append(product)
    sliced_result = []
    for index in range(1, len(result)):
        element = result[index]
        sliced_result.append(element)
    return sliced_result