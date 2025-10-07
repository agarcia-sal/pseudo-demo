def derivative(xs: list):
    result = [None]
    for index in range(len(xs)):
        coefficient = xs[index]
        product = index * coefficient
        result.append(product)
    sliced_result = [None]
    for index in range(1, len(result)):
        element = result[index]
        sliced_result.append(element)
    return sliced_result