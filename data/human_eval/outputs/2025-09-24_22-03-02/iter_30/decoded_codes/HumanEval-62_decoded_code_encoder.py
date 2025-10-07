def derivative(xs: list) -> list:
    result = [0]
    index = 0
    while index < len(xs):
        product = index * xs[index]
        result.append(product)
        index += 1
    result = result[1:len(result)-1]
    return result