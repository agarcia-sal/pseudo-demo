def derivative(xs: list) -> list:
    result_list = []
    for i in range(len(xs)):
        x = xs[i]
        product = i * x
        result_list.append(product)
    derivative_list = []
    for j in range(1, len(result_list)):
        element = result_list[j]
        derivative_list.append(element)
    return derivative_list