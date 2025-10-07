def derivative(xs: list):
    result = []
    for index, value in enumerate(xs):
        result.append(index * value)
    return result[1:]