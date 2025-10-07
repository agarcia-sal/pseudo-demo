def derivative(xs: list):
    result = []
    for i in range(len(xs)):
        temp = i * xs[i]
        result.append(temp)
    return result[1:]