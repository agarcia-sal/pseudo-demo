def derivative(xs: list) -> list:
    result = [0]
    for i in range(len(xs)):
        x = xs[i]
        product = i * x
        result.append(product)
    sliced_result = [result[index] for index in range(1, len(result))]
    return sliced_result